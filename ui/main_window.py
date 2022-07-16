"""
Nick Depatie
Assignment Database GUI
This script will create a GUI to allow the user to log assignments to a database, 
    access the items in the database, and sort the items by urgency using merge sort 
    (i.e. how close the deadline is and how important is the assignment)
"""

from os import DirEntry
import sys
import time
import importlib
from typing import Text
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QListWidgetItem, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QLineEdit, 
    QListWidget, 
    QCompleter, 
    QCalendarWidget,
    QScrollBar,
    QComboBox
    )
from PyQt5.QtGui import QColor, QIcon, QPainter
from PyQt5.QtCore import center, pyqtSlot, QDate, QRect
from PyQt5.sip import assign
import database_interface as interface
import process_assignments as process

def MainWindow(QWidget):
    
    widget = QWidget()

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

    global calendar
    calendar=QCalendarWidget(widget)
    calendar.setGeometry(600, 270, 775, 600)
    calendar.selectionChanged.connect(calendar_date)

    global timelistwidget
    timelistwidget=QListWidget(widget)
    timelistwidget.setGeometry(1400, 317, 200, 555)
    timescrollbar=QScrollBar(widget)
    timelistwidget.setVerticalScrollBar(timescrollbar)
    insertTimes()
    timelistwidget.itemSelectionChanged.connect(selecttime)

    welcomewidget=QLabel(widget)
    welcomewidget.setText("Welcome User, What would you like to accomplish today?")
    welcomewidget.move(200,10)

    assignmentlabel=QLabel(widget)
    assignmentlabel.setText("Assignment Name")
    assignmentlabel.move(850,150)

    subjectlabel=QLabel(widget)
    subjectlabel.setText("Subject Name")
    subjectlabel.move(600,150)

    datelabel=QLabel(widget)
    datelabel.setText("Priority (0-10)")
    datelabel.move(1100,150)

    timelabel=QLabel(widget)
    timelabel.setText("Time")
    timelabel.move(1400,280)

    global assignmentnameinput
    assignmentnameinput=QLineEdit(widget)
    assignmentnameinput.setGeometry(850, 190, 200, 50)

    global subjectinput
    subjectinput=QLineEdit(widget)
    subjectinput.setGeometry(600, 190, 200, 50)

    courses=["DiffEq","Circuits","Organization","Embedded","Co-op"]
    completer=QCompleter(courses,widget)
    #completer.setCaseSensitivity(Qt.CaseInsensitive)
    subjectinput.setCompleter(completer)



    global priorityinput
    priorityinput=QLineEdit(widget)
    priorityinput.setGeometry(1100, 190, 200, 50)
    
    global listwidget
    listwidget=QListWidget(widget)
    listwidget.setGeometry(50,150,500,500)
    listwidget.doubleClicked.connect(removeassignments)

    getassignments()

    widget.setGeometry(250,250,1625,1000)
    widget.setWindowTitle("Assignment Workspace")
    widget.show()

    sys.exit(app.exec_())