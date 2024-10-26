import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from game_ui import Ui_MainWindow 
from puzzle import Puzzle
from solver_factory import SolverFactory
import time

class PuzzleGame(QMainWindow):
    def __init__(self):
        super(PuzzleGame, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)  
        self.setup_connections()

    def setup_connections(self):
        self.ui.pushButton_solve.clicked.connect(self.solve_game)
        self.ui.pushButton_shuffle.clicked.connect(self.shuffle_puzzle)
        for button in self.ui.buttons:
            button.clicked.connect(lambda _, b=button: self.button_clicked(b))

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
        if(not self.validate_input()):
            return
        self.ui.pushButton_solve.setEnabled(False)
        self.ui.pushButton_shuffle.setEnabled(False)
        initial_state = self.ui.lineEdit.text()
        solver_strategy = self.ui.comboBox.currentText()
        self.update_puzzle_state(initial_state)
        QApplication.processEvents()
        time.sleep(2)
        puzzle = Puzzle(initial_state)
        solver = SolverFactory.create_solver(puzzle, solver_strategy)
        result = solver.solve(puzzle)
        
        # Display the movements (states) in the UI
        # for state in result.path_to_goal:
        #     self.update_puzzle_state(state)
        #     QApplication.processEvents()
        #     time.sleep(1)  # Add delay to visualize the movements

        path = {"120453768", "123405768", "123450768", "123456708", "123456780", 
                "123456708", "123450768", "123405768", "120453768"}
        
        for state in path:
            self.update_puzzle_state(state)
            QApplication.processEvents()
            time.sleep(1)
        
        self.ui.lineEdit.setText("")
        self.ui.pushButton_solve.setEnabled(True)
        self.ui.pushButton_shuffle.setEnabled(True)
        for button in self.ui.buttons:
            button.setEnabled(True)
        # Add code to display the res ults in the UI here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PuzzleGame()
    window.show()
    sys.exit(app.exec_())

# from strategies.bfs_solver import BFSSolver
# from solver_factory import SolverFactory
# from puzzle import Puzzle

# def test_bfs_solver():
#     puzzle = Puzzle("876543210")
#     solver = SolverFactory.create_solver(puzzle, 'bfs')
#     solver.start_timer()
#     shortest_path = solver.solve()
#     result = solver.path_results(shortest_path)
#     print(f"Shortest Path:{result.path_to_goal}\nCost of the path:{result.cost_of_path}\nNodes Expanded:{result.nodes_expanded}\nSearch Depth:{result.search_depth}\nRunning time:{result.running_time}")

# if __name__ == "__main__":
#     test_bfs_solver()

