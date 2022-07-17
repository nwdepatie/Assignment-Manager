from PyQt6.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QCompleter, 
    QVBoxLayout,
    QComboBox,
    QMenuBar
    )
from PyQt6.QtGui import QColor, QIcon, QPainter


class MenuBarWidget(QMenuBar):

    def __init__(self):
        super().__init__()
        self.addMenu("LOG ASSIGNMENT")
        self.addMenu("Pull Assignments")
        self.addMenu("Initialize Table")