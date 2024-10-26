from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.buttons = []
                for i in range(9):
                        button = QtWidgets.QPushButton(self.widget)
                        button.setObjectName(f"pushButton_{i}")
                        self.buttons.append(button)
                        
                
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(803, 694)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.pushButton_shuffle = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_shuffle.setGeometry(QtCore.QRect(540, 150, 251, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_shuffle.setFont(font)
                self.pushButton_shuffle.setStyleSheet("QPushButton {\n"
        "    background-color: orange;  /* Green background */\n"
        "    color: white;               /* White text */\n"
        "    border-radius: 10px;        /* Rounded corners */\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #ff5722; /* When hovered */\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #e64a19; /* When pressed */\n"
        "}")
                self.pushButton_shuffle.setObjectName("pushButton")
                self.comboBox = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox.setGeometry(QtCore.QRect(660, 10, 131, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.comboBox.setFont(font)
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(540, 100, 251, 31))
                self.lineEdit.setObjectName("lineEdit")
                self.label_strategy = QtWidgets.QLabel(self.centralwidget)
                self.label_strategy.setGeometry(QtCore.QRect(540, 10, 101, 31))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_strategy.setFont(font)
                self.label_strategy.setObjectName("label")
                self.label_custom_state = QtWidgets.QLabel(self.centralwidget)
                self.label_custom_state.setGeometry(QtCore.QRect(540, 60, 141, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_custom_state.setFont(font)
                self.label_custom_state.setObjectName("label_custom_state")
                self.pushButton_solve = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_solve.setGeometry(QtCore.QRect(540, 230, 251, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_solve.setFont(font)
                self.pushButton_solve.setStyleSheet("QPushButton {\n"
        "    background-color: lightgreen;  /* Green background */\n"
        "    color: white;               /* White text */\n"
        "    border-radius: 10px;        /* Rounded corners */\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #45a049; /* When hovered */\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #3e8e41; /* When pressed */\n"
        "}")
                self.pushButton_solve.setObjectName("pushButton_solve")
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(0, 10, 531, 531))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
                self.widget.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setPointSize(30)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.widget.setFont(font)
                self.widget.setMouseTracking(True)
                self.widget.setObjectName("widget")
                self.gridLayout = QtWidgets.QGridLayout(self.widget)
                self.gridLayout.setContentsMargins(5, 5, 5, 5)
                self.gridLayout.setSpacing(5)
                self.gridLayout.setObjectName("gridLayout")
        
                self.buttons[5].setObjectName("buttons[5]")
                self.gridLayout.addWidget(self.buttons[5], 1, 2, 1, 1)
        
                self.buttons[8].setObjectName("buttons[8]")
                self.gridLayout.addWidget(self.buttons[8], 2, 2, 1, 1)
        
                self.buttons[7].setObjectName("buttons[7]")
                self.gridLayout.addWidget(self.buttons[7], 2, 1, 1, 1)
        
                self.buttons[4].setObjectName("buttons[4]")
                self.gridLayout.addWidget(self.buttons[4], 1, 1, 1, 1)
        
                self.buttons[6].setObjectName("buttons[6]")
                self.gridLayout.addWidget(self.buttons[6], 2, 0, 1, 1)
        
                self.buttons[0].setText("")
                self.buttons[0].setObjectName("buttons[0]")
                self.gridLayout.addWidget(self.buttons[0], 0, 0, 1, 1)
        
                self.buttons[3].setObjectName("buttons[3]")
                self.gridLayout.addWidget(self.buttons[3], 1, 0, 1, 1)

                self.buttons[1].setObjectName("pushButton_1")
                self.gridLayout.addWidget(self.buttons[1], 0, 1, 1, 1)
                self.buttons[2].setObjectName("buttons[2]")
                self.gridLayout.addWidget(self.buttons[2], 0, 2, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                for i in range(9):
                        self.setup_button(self.buttons[i])
                self.buttons[0].setStyleSheet("")

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.pushButton_shuffle.setText(_translate("MainWindow", "Shuffle"))
                self.comboBox.setItemText(0, _translate("MainWindow", "DFS"))
                self.comboBox.setItemText(1, _translate("MainWindow", "BFS"))
                self.comboBox.setItemText(2, _translate("MainWindow", "IDS"))
                self.comboBox.setItemText(3, _translate("MainWindow", "A*_Manhattan"))
                self.comboBox.setItemText(4, _translate("MainWindow", "A*_Euclidean"))
                self.label_strategy.setText(_translate("MainWindow", "Stragety"))
                self.label_custom_state.setText(_translate("MainWindow", "Custom state"))
                self.pushButton_solve.setText(_translate("MainWindow", "Solve"))
                self.buttons[0].setText(_translate("MainWindow", ""))
                self.buttons[5].setText(_translate("MainWindow", "5"))
                self.buttons[8].setText(_translate("MainWindow", "8"))
                self.buttons[7].setText(_translate("MainWindow", "7"))
                self.buttons[4].setText(_translate("MainWindow", "4"))
                self.buttons[6].setText(_translate("MainWindow", "6"))
                self.buttons[3].setText(_translate("MainWindow", "3"))
                self.buttons[1].setText(_translate("MainWindow", "1"))
                self.buttons[2].setText(_translate("MainWindow", "2"))
        
        def setup_button(self, button):
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                button.setSizePolicy(sizePolicy)
                palette = QtGui.QPalette()
                font = QtGui.QFont()
                font.setPointSize(30)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                button.setFont(font)
                button.setMouseTracking(True)
                button.setStyleSheet("QPushButton {\n"
        "    background-color: #29b6f6;  /* Green background */\n"
        "    color: white;               /* White text */\n"
        "    border-radius: 10px;        /* Rounded corners */\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #039be5; /* When hovered */\n"
        "}\n"
        "")


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())