from PyQt6.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout,
    QComboBox
    )
from PyQt6.QtGui import QColor, QIcon, QPainter


class PriorityInputLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Input Priority (1-10)")


class PriorityInputComboBox(QComboBox):
    validUserInput = 1
    prioritylist = ['1','2','3','4','5','6','7','8','9','10']

    def __init__(self):
        super().__init__()
        self.addItems(self.prioritylist)
        self.setStyleSheet("QComboBox { background-color: white; }")

    def cleanseInput(self,userInput):
        if self.hasAcceptableInput() and userInput < 10:
            self.validUserInput = userInput
        else:
            self.clear()
            self.setText(self.validUserInput)

class PriorityInputWidget(QWidget):
    label = None
    comboBox = None

    def __init__(self):
        super().__init__()
        self.label = PriorityInputLabel()
        self.comboBox = PriorityInputComboBox()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)

        self.setLayout(layout)