from PyQt6.QtWidgets import (
    QCalendarWidget,
    QComboBox
    )
from ui.widgets.stylesheets import ROUNDED_GREY_WIDGET

class DateInputWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#1F1F1E;")
        