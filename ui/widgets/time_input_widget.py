from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QListWidget, 
    QScrollBar,
    QVBoxLayout
    )

class TimeSelectionLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText('Select Time Due')

class TimeSelectionList(QListWidget):
    def __init__(self):
        super().__init__()
        scrollBar = QScrollBar()
        self.setVerticalScrollBar(scrollBar)
        self.initializeTimes()

    def initializeTimes(self):
        j=0
        for i in range(0,24):
            if i<=12:
                if i!=12:
                    if i==0:
                        i=12
                    self.insertItem(j,str(i)+":00 AM")
                    j +=1
                    self.insertItem(j,str(i)+":30 AM")
                    j +=1
                else:
                    self.insertItem(j,str(i)+":00 PM")
                    j +=1
                    self.insertItem(j,str(i)+":30 PM")
                    j +=1
            else:
                self.insertItem(j,str(i-12)+":00 PM")
                j +=1
                self.insertItem(j,str(i-12)+":30 PM")
                j +=1
        self.insertItem(j,"11:59 PM")

class TimeInputWidget(QWidget):
    label = None
    selectionList = None

    def __init__(self):
        super().__init__()
        self.label = TimeSelectionLabel()
        self.selectionList = TimeSelectionList()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.selectionList)
        self.setLayout(layout)
