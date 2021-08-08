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
    QListWidgetItem, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QLineEdit, 
    QListWidget, 
    QCompleter, 
    QCalendarWidget,
    QScrollBar
    )
from PyQt5.QtGui import QColor, QIcon, QPainter
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
    calendar.selectionChanged.connect(calendar_date)

    global timelistwidget
    timelistwidget=QListWidget(widget)
    timelistwidget.setGeometry(1325, 317, 200, 555)
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
    timelabel.move(1325,280)

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
    listwidget.doubleClicked.connect(removeassignments)

    getassignments()

    widget.setGeometry(250,250,1600,1000)
    widget.setWindowTitle("Assignment Workspace")
    widget.show()

    sys.exit(app.exec_())

#############################################################################################

def logassignments():
    print("logging assignment...")
    subject=subjectinput.text()
    assignmentname=assignmentnameinput.text()
    priority=priorityinput.text()
    try:
        due_date=int(due_date_date+due_date_time)
        interface.send.push_assignments(subject, assignmentname, due_date, priority)
    except:
        print("error logging entry: part of due date was not given")
    finally:
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
        assignment=QListWidgetItem('%s' % process.process.getsublist(assignmentlist[i],0))

        urgency=int(process.process.getsublist(assignmentlist[i],1))

        if urgency > 50000:
            assignment.setBackground(QColor('#C1E1C1'))

        if urgency < 50000 and urgency > 10000:
            assignment.setBackground(QColor('#fdfd96'))

        if urgency < 10000:
            assignment.setBackground(QColor('#ff6961'))

        listwidget.addItem(assignment)
        
    
    print("done getting!")

def removeassignments():
    print(listwidget.currentRow())

def init_table():
    print("initializing table...")
    interface.initialize.initialize()
    logassignments()

def calendar_date():
    global due_date_date
    due_date_date=QDate.toString(calendar.selectedDate())
    due_date_date=process.process.datetoint(due_date_date)

def selecttime():
    global due_date_time
    due_date_time=timelist[timelistwidget.currentRow()]
    if len(due_date_time)==3:
        due_date_time="0"+due_date_time

def insertTimes():
    global timelist
    timelist=[]
    j=0
    for i in range(0,24):
        if i<=12:
            if i!=12:
                if i==0:
                    i=12
                timelistwidget.insertItem(j,str(i)+":00 AM")
                timelist.append(str(i)+"00")
                j +=1
                timelistwidget.insertItem(j,str(i)+":30 AM")
                timelist.append(str(i)+"30")
                j +=1
            else:
                timelistwidget.insertItem(j,str(i)+":00 PM")
                timelist.append(str(i)+"00")
                j +=1
                timelistwidget.insertItem(j,str(i)+":30 PM")
                timelist.append(str(i)+"30")
                j +=1
        else:
            timelistwidget.insertItem(j,str(i-12)+":00 PM")
            timelist.append(str(i)+"00")
            j +=1
            timelistwidget.insertItem(j,str(i-12)+":30 PM")
            timelist.append(str(i)+"30")
            j +=1
    timelistwidget.insertItem(j,"11:59 PM")
    timelist.append("2359")
    timelist[0]="0000"
    timelist[1]="0030"

################################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow()