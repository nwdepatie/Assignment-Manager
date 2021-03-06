"""
Nick Depatie
Assignment Database GUI
This script will create a GUI to allow the user to log assignments to a database, 
    access the items in the database, and sort the items by urgency using merge sort 
    (i.e. how close the deadline is and how important is the assignment)
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
    )
from ui.widgets.user_input_widget import UserInputWidget
from ui.widgets.menu_bar_widget import MenuBarWidget

'''
def mainWindow():

    sortbutton = QPushButton(widget)
    sortbutton.setText("Sort All Assignments")
    sortbutton.setGeometry(50,64,275,55)
    sortbutton.clicked.connect(getassignments)

    logbutton = QPushButton(widget)
    logbutton.setText("Log Assignment")
    logbutton.setGeometry(350,64,275,55)
    logbutton.clicked.connect(logassignments)

    initbutton = QPushButton(widget)
    initbutton.setText("Initilialize Table")
    initbutton.setGeometry(650,64,275,55)
    initbutton.clicked.connect(init_table)

    welcomewidget=QLabel(widget)
    welcomewidget.setText("Welcome User, What would you like to accomplish today?")
    welcomewidget.move(200,10)

    widget.setWindowTitle("Assignment Workspace")
    widget.show()
'''

class MainWindow(QWidget):
    userInput = None
    menuBar = None

    def __init__(self):
        super().__init__()
        self.userInput = UserInputWidget()
        self.menuBar = MenuBarWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.menuBar)
        layout.addWidget(self.userInput)
        self.setLayout(layout)
        self.show()