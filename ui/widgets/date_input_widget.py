from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QListWidgetItem, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QLineEdit, 
    QListWidget, 
    QCompleter, 
    QCalendarWidget,
    QScrollBar,
    QComboBox
    )

class DateInputWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()