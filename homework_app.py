"""
Nick Depatie
Assignment Database GUI
This script will create a GUI to allow the user to log assignments to a database, 
    access the items in the database, and sort the items by urgency using merge sort 
    (i.e. how close the deadline is and how important is the assignment)
"""

from datetime import datetime
from os import DirEntry
import sys
import time
import importlib
from typing import Text
import PyQt6
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QListWidgetItem,
    QMainWindow, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QLineEdit, 
    QListWidget, 
    QCompleter, 
    QCalendarWidget,
    QScrollBar,
    QComboBox,
    QVBoxLayout
    )
from PyQt6.QtGui import QColor, QIcon, QPainter
from PyQt6.QtCore import center, pyqtSlot, QDate, QRect
from PyQt6.sip import assign
import database_interface as interface
import process_assignments as process
import googlecalendar_interface as quickstart


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(250,250,2000,900)
        self.setWindowTitle("Assignment Workspace")
        self.UiComponents()
        self.show()

    def UiComponents(self):

        #sortbutton = QPushButton(self)
        #sortbutton.setText("Sort All Assignments")
        #sortbutton.setGeometry(50,64,275,55)
        #sortbutton.clicked.connect(mainWindow.getassignments)

        logbutton = QPushButton(self)
        logbutton.setText("Log Assignment")
        logbutton.setGeometry(50,64,275,55)
        logbutton.clicked.connect(mainWindow.logassignments)

        initbutton = QPushButton(self)
        initbutton.setText("Initilialize Table")
        initbutton.setGeometry(350,64,275,55)
        initbutton.clicked.connect(mainWindow.init_table)

        todobutton=QPushButton(self)
        todobutton.setText("To Do:")
        todobutton.setGeometry(1600,64,100,55)
        todobutton.clicked.connect(mainWindow.logtodo)

        global calendar, due_date_date
        calendar=QCalendarWidget(self)
        calendar.setGeometry(600, 270, 775, 600)

        global timelistwidget
        timelistwidget=QListWidget(self)
        timelistwidget.setGeometry(1400, 317, 200, 555)
        timescrollbar=QScrollBar(self)
        timelistwidget.setVerticalScrollBar(timescrollbar)
        mainWindow.insertTimes()
        timelistwidget.itemSelectionChanged.connect(mainWindow.selecttime)

        welcomewidget=QLabel(self)
        welcomewidget.setText("Welcome User, What would you like to accomplish today?")
        welcomewidget.setGeometry(50,0,1000,60)

        assignmentlabel=QLabel(self)
        assignmentlabel.setText("Assignment Name")
        assignmentlabel.setGeometry(850,150,215,50)

        subjectlabel=QLabel(self)
        subjectlabel.setText("Subject Name")
        subjectlabel.setGeometry(600,150,215,50)

        datelabel=QLabel(self)
        datelabel.setText("Priority (1-10)")
        datelabel.setGeometry(1100,150,215,50)

        timelabel=QLabel(self)
        timelabel.setText("Time")
        timelabel.move(1400,280)

        global assignmentnameinput
        assignmentnameinput=QLineEdit(self)
        assignmentnameinput.setGeometry(850, 190, 200, 50)

        global subjectinput
        subjectinput=QLineEdit(self)
        subjectinput.setGeometry(600, 190, 200, 50)
        courses=["DiffEq","Circuits","Organization","Embedded","Co-op"]
        completer=QCompleter(courses,self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        subjectinput.setCompleter(completer)

        global priorityinput
        priorityinput=QComboBox(self)
        prioritylist=['1','2','3','4','5','6','7','8','9','10']
        priorityinput.addItems(prioritylist)
        priorityinput.setStyleSheet("QComboBox { background-color: white; }")
        priorityinput.setGeometry(1100, 190, 200, 50)

        global todoinput
        todoinput=QLineEdit(self)
        todoinput.setGeometry(1715, 64, 250, 50)
        
        global assignmentlistwidget
        assignmentlistwidget=QListWidget(self)
        assignmentlistwidget.setGeometry(50,150,500,720)
        assignmentlistwidget.doubleClicked.connect(mainWindow.removeassignments)

        global todolistwidget
        todolistwidget=QListWidget(self)
        todolistwidget.setGeometry(1650, 150, 300, 720)
        todolistwidget.doubleClicked.connect(mainWindow.removetodo)

        mainWindow.getassignments()
        mainWindow.gettodos()
        try:
            quickstart.init()
        except:
            print("unable to access Google Calendar")

    def logassignments():
        print("logging assignment...")
        subject=subjectinput.text()
        assignmentname=assignmentnameinput.text()
        priority=priorityinput.currentText()
        due_date_object=datetime.strptime(QDate.toString(calendar.selectedDate()),"%a %b %d %Y")
        due_date_date=due_date_object.month*1000000+due_date_object.day*10000
        try:
            due_date=int(due_date_date+due_date_time)
            interface.assignmentdatabase.push_assignments(subject, assignmentname, due_date, priority)
            quickstart.log_assignment(subject, assignmentname)
        except:
            print("error logging entry: part of due date was not given")
        finally:
            subjectinput.clear()
            assignmentnameinput.clear()
            importlib.reload(interface)
            mainWindow.getassignments()
            print("done logging!")

    def getassignments():
        global assignmentlist
        print("processing assignments...")
        assignmentlistwidget.clear()
        importlib.reload(interface)
        assignmentlist=interface.assignmentdatabase.callassignments()
        process.process.string_to_int(assignmentlist)
        process.process.mergesort_list(assignmentlist)
        process.process.weeks_sorting(assignmentlist)
        
        for i in range (len(assignmentlist)):
            assignment=QListWidgetItem('%s' % process.process.getsublist(assignmentlist[i],0))

            try:
                urgency=int(process.process.getsublist(assignmentlist[i],1))

                if urgency >= 50000:
                    assignment.setBackground(QColor('#C1E1C1'))

                if urgency < 50000 and urgency >= 10000:
                    assignment.setBackground(QColor('#fdfd96'))

                if urgency < 10000 and urgency >=-10000:
                    assignment.setBackground(QColor('#ff6961'))
                
                if urgency <-10000:
                    assignment.setBackground(QColor('#C3B1E1'))
            except:
                assignment=QListWidgetItem('%s' % "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            finally:
                assignmentlistwidget.addItem(assignment)
            
        
        print("done getting!")

    def removeassignments():
        try:
            assignment,subject=process.process.getsublist(assignmentlist[assignmentlistwidget.currentRow()],3)
            print("deleting assignment...")
            interface.assignmentdatabase.delete_assignments(assignment,subject)
            mainWindow.getassignments()
            print("done deleting!")
        except:
            print("unable to delete item!")

    def init_table():
        print("initializing table...")
        quickstart.init()
        interface.assignmentdatabase.initialize()
        mainWindow.getassignments()

    def selecttime():
        global due_date_time
        due_date_time=int(timelist[timelistwidget.currentRow()])

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

    def logtodo():
        print("logging assignment...")
        name=todoinput.text()
        try:
            interface.tododatabase.push_todo(name)
        except:
            print("error logging entry: part of due date was not given")
        finally:
            todoinput.clear()
            importlib.reload(interface)
            mainWindow.gettodos()
            print("done logging!")

    def gettodos():
        global todolist
        print("processing todos...")
        todolistwidget.clear()
        importlib.reload(interface)
        todolist=interface.tododatabase.calltodos()

        for i in range (len(todolist)):
            todo=QListWidgetItem('%s' % process.process.getsublist(todolist[i],0))
            if i%2==1:
                todo.setBackground(QColor('#C9CFD6'))
            todolistwidget.addItem(todo)

    def removetodo():
        try:
            name=process.process.getsublist(todolist[todolistwidget.currentRow()],0)
            print("deleting assignment...")
            interface.tododatabase.delete_todo(name[0])
            mainWindow.gettodos()
            print("done deleting!")
        except:
            print("unable to delete item!")

################################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=mainWindow()
    sys.exit(app.exec())
