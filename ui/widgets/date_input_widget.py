from PyQt6.QtWidgets import (
    QCalendarWidget,
    QComboBox
    )

class DateInputWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()