from readline import set_completer
from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout
    )
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
        #completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompleter(completer)


class SubjectInputWidget(QWidget):
    lineEdit = SubjectInputLineEdit()
    label    = SubjectInputLabel()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)