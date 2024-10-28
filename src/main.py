import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
from game_ui import Ui_MainWindow 
from puzzle import Puzzle
from result import Result
from solver_factory import SolverFactory
import time


class ResultDialog(QtWidgets.QDialog):
    def __init__(self, result, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Solution Result")
        self.setMinimumSize(600, 450)
        
        # Main layout
        layout = QtWidgets.QVBoxLayout()
        
        # Display result details using existing attributes
        result_layout = QtWidgets.QFormLayout()
        
        path_label = QtWidgets.QLabel("Path to Goal:")
        path_list = QtWidgets.QListWidget()
        for step in result.path_to_goal:
            path_list.addItem(step)
        path_list.setFixedHeight(200)
        
        cost_label = QtWidgets.QLabel("Path Cost:")
        cost_value = QtWidgets.QLabel(str(result.cost_of_path))
        
        expanded_label = QtWidgets.QLabel("Nodes Expanded:")
        expanded_value = QtWidgets.QLabel(str(result.nodes_expanded))
        
        depth_label = QtWidgets.QLabel("Search Depth:")
        depth_value = QtWidgets.QLabel(str(result.search_depth))
        
        runtime_label = QtWidgets.QLabel("Running Time:")
        runtime_value = QtWidgets.QLabel(f"{result.running_time:.4f} seconds")
        
        # Setting font for readability
        font_title = QtGui.QFont()
        font_title.setPointSize(13)
        font_title.setBold(True)

        font_value = QtGui.QFont()
        font_value.setPointSize(13)
        font_value.setBold(True)

        # Title labels
        for label in [path_label, cost_label, expanded_label, depth_label, runtime_label]:
            label.setFont(font_title)
            label.setStyleSheet("color: #8B008B")  # Dark mauve for titles

        # Value labels
        for label in [cost_value, expanded_value, depth_value, runtime_value]:
            label.setFont(font_value)
            label.setStyleSheet("color: darkgreen")  # Dark green for values

        # Adding widgets to the form layout
        result_layout.addRow(path_label, path_list)
        result_layout.addRow(cost_label, cost_value)
        result_layout.addRow(expanded_label, expanded_value)
        result_layout.addRow(depth_label, depth_value)
        result_layout.addRow(runtime_label, runtime_value)

        # Adding form layout to the main layout
        layout.addLayout(result_layout)

        # Set layout to dialog
        self.setLayout(layout)

        # Customize the font for the items in the QListWidget
        font_state = QtGui.QFont()
        font_state.setPointSize(12)
        font_state.setBold(True)

        for i in range(path_list.count()):
            item = path_list.item(i)
            item.setFont(font_state)


class PuzzleGame(QMainWindow):
    def __init__(self):
        super(PuzzleGame, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)  
        self.setup_connections()
        self.result = None
        self.current_step = 0
        self.path = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_next_state)

    def setup_connections(self):
        self.ui.pushButton_solve.clicked.connect(self.solve_game)
        self.ui.pushButton_shuffle.clicked.connect(self.shuffle_puzzle)
        self.ui.pushButton_show_result.clicked.connect(self.show_result_dialog)
        self.ui.pushButton_prev.clicked.connect(self.show_prev_state)
        self.ui.pushButton_next.clicked.connect(self.show_next_state)
        self.ui.pushButton_speed.pressed.connect(self.start_speed)
        self.ui.pushButton_speed.released.connect(self.stop_speed)
        for button in self.ui.buttons:
            button.clicked.connect(lambda _, b=button: self.button_clicked(b))

    def show_result_dialog(self):
        if self.result:
            dialog = ResultDialog(self.result, self)
            dialog.exec_()

    def button_clicked(self, button):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + (button.text() if button.text() else "0"))
        button.setEnabled(False)        

    def validate_input(self):
        self.ui.lineEdit.setReadOnly(True)
        if set(self.ui.lineEdit.text()) != set("012345678"):
            self.ui.lineEdit.setText("Invalid input")
            QTimer.singleShot(2000, self.reset_line_edit)
            for button in self.ui.buttons:
                button.setEnabled(True)
            return False
        elif not Puzzle.is_solvable(self.ui.lineEdit.text()):
            self.ui.lineEdit.setText("unsolvable!!")
            QTimer.singleShot(2000, self.reset_line_edit)
            for button in self.ui.buttons:
                button.setEnabled(True)
            return False
        else:
            self.ui.pushButton_solve.setEnabled(True)
            self.ui.pushButton_shuffle.setEnabled(True)
            self.ui.lineEdit.setReadOnly(False)
            return True
    
    def reset_line_edit(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setReadOnly(False)

    def update_puzzle_state(self, state):
        for i in range(9):
            if state[i] == '0':
                self.ui.buttons[i].setText("")
                self.ui.buttons[i].setStyleSheet("")
            else:
                self.ui.buttons[i].setText(state[i])
                self.ui.buttons[i].setStyleSheet("QPushButton {\n"
                "    background-color: #29b6f6;  /* Green background */\n"
                "    color: white;               /* White text */\n"
                "    border-radius: 10px;        /* Rounded corners */\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: #039be5; /* When hovered */\n"
                "}\n"
                "")
                        
    def shuffle_puzzle(self):
        new_state = Puzzle.generate_solvable_state()
        self.update_puzzle_state(new_state)
        self.ui.lineEdit.setText(new_state)

    def solve_game(self):
        if not self.validate_input():
            return
        self.ui.pushButton_solve.setEnabled(False)
        self.ui.pushButton_shuffle.setEnabled(False)
        initial_state = self.ui.lineEdit.text()
        solver_strategy = self.ui.comboBox.currentText()
        self.update_puzzle_state(initial_state)
        QApplication.processEvents()
        puzzle = Puzzle(initial_state)
        solver = SolverFactory.create_solver(puzzle, solver_strategy)
        self.result = solver.solve()
        
        self.path = self.result.path_to_goal
        self.current_step = 0
        
        print(f"Cost of path: {self.result.cost_of_path}" 
              f"\nNodes expanded: {self.result.nodes_expanded}\nMax search depth: {self.result.search_depth}"
              f"\nTime taken: {self.result.running_time} seconds")

        if self.path:
            self.update_puzzle_state(self.path[self.current_step])
        
        self.ui.lineEdit.setText("")
        self.ui.pushButton_solve.setEnabled(True)
        self.ui.pushButton_shuffle.setEnabled(True)
        for button in self.ui.buttons:
            button.setEnabled(True)

    def show_prev_state(self):
        if self.path and self.current_step > 0:
            self.current_step -= 1
            self.update_puzzle_state(self.path[self.current_step])

    def show_next_state(self):
        if self.path and self.current_step < len(self.path) - 1:
            self.current_step += 1
            self.update_puzzle_state(self.path[self.current_step])

    def start_speed(self):
        self.timer.start(100)  # Adjust the interval as needed (100ms = 0.1s)

    def stop_speed(self):
        self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PuzzleGame()
    window.show()
    sys.exit(app.exec_())
