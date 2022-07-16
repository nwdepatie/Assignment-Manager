from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout
    )
from PyQt5.QtGui import QColor, QIcon, QPainter


class AssignmentNameInputLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText('Input Assignment Name')


class AssignmentNameInputLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()


class AssignmentNameInputWidget(QWidget):
    lineEdit = None
    label    = None

    def __init__(self):
        super().__init__()
        self.lineEdit = AssignmentNameInputLineEdit()
        self.label    = AssignmentNameInputLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)