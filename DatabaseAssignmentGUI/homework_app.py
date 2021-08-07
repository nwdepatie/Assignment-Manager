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
    QWidget, 
    QPushButton, 
    QLabel, 
    QLineEdit, 
    QListWidget, 
    QCompleter, 
    QCalendarWidget,
    )
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import center, pyqtSlot, QDate, QRect
from PyQt5.sip import assign
import database_interface as interface
import process_assignments as process

def mainwindow():
    
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
    calendar.setGeometry(600, 270, 700, 600)
    calendar.selectionChanged.connect(lambda:calendar_date())

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
    datelabel.setText("Priority (1-10)")
    datelabel.move(1100,150)

    global assignmentnameinput
    assignmentnameinput=QLineEdit(widget)
    assignmentnameinput.setGeometry(850, 190, 200, 50)

    global subjectinput
    subjectinput=QLineEdit(widget)
    subjectinput.setGeometry(600, 190, 200, 50)

    global priorityinput
    priorityinput=QLineEdit(widget)
    priorityinput.setGeometry(1100, 190, 200, 50)
    
    global listwidget
    listwidget=QListWidget(widget)
    listwidget.setGeometry(50,150,500,500)

    widget.setGeometry(250,250,1500,1000)
    widget.setWindowTitle("Assignment Workspace")
    widget.show()

    sys.exit(app.exec_())

#############################################################################################


def logassignments():
    print("logging assignment...")
    subject=subjectinput.text()
    assignmentname=assignmentnameinput.text()
    priority=priorityinput.text()
    interface.send.push_assignments(subject, assignmentname, due_date, priority)
    subjectinput.clear()
    assignmentnameinput.clear()
    priorityinput.clear()
    importlib.reload(interface)
    getassignments()
    print("done logging!")
    
def getassignments():
    print("processing assignments...")
    listwidget.clear()
    importlib.reload(interface)
    assignmentlist=interface.receive.callassignments()
    process.process.string_to_int(assignmentlist)
    process.process.mergesort_list(assignmentlist)
    
    for i in range (len(assignmentlist)):
        assignment=process.process.getsublist(assignmentlist[i],0)
        listwidget.insertItem(i,str(assignment))
    
    print("done getting!")

def init_table():
    print("initializing table...")
    interface.initialize.initialize()

def calendar_date():
    global due_date
    due_date=QDate.toString(calendar.selectedDate())
    due_date=process.process.timetoint(due_date)

################################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow()