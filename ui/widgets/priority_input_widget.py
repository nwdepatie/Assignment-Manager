from readline import set_completer
from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout
    )
from PyQt5.QtGui import QColor, QIcon, QPainter


class PriorityInputLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Input Priority (1-10)")


class PriorityInputLineEdit(QLineEdit):
    validUserInput = 1
    ONLY_NUMBERS_ALLOWED = '9D' # Only numbers  greater than 0 allowed

    def __init__(self):
        super().__init__()
        self.setInputMask(self.ONLY_NUMBERS_ALLOWED)
        self.textChanged.connect(self.cleanseInput)

    def cleanseInput(self,userInput):
        if self.hasAcceptableInput() and userInput < 10:
            self.validUserInput = userInput
        else:
            self.clear()
            self.setText(self.validUserInput)


class PriorityInputWidget(QWidget):
    label = PriorityInputLabel()
    lineEdit = PriorityInputLineEdit()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)