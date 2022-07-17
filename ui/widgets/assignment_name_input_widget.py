from PyQt6.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout
    )
from PyQt6.QtGui import QColor, QIcon, QPainter
from ui.widgets.stylesheets import BRIGHT_TEXT_LABEL, ROUNDED_GREY_WIDGET


class AssignmentNameInputLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText('Input Assignment Name')
        self.setStyleSheet(BRIGHT_TEXT_LABEL)


class AssignmentNameInputLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(ROUNDED_GREY_WIDGET)


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