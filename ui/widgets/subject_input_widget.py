from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout
    )
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QIcon, QPainter


class SubjectInputLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText('Input Subject')


class SubjectInputLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setCompleterKeywords([])

    def setCompleterKeywords(self,wordList):
        completer=QCompleter(wordList)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompleter(completer)


class SubjectInputWidget(QWidget):
    lineEdit = None
    label    = None

    def __init__(self):
        super().__init__()
        self.lineEdit = SubjectInputLineEdit()
        self.label    = SubjectInputLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)