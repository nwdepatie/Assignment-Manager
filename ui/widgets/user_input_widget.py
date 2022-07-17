from PyQt6.QtWidgets import (
    QWidget, 
    QHBoxLayout,
    QVBoxLayout
    )
from ui.widgets.date_input_widget import DateInputWidget
from ui.widgets.assignment_name_input_widget import AssignmentNameInputWidget
from ui.widgets.priority_input_widget import PriorityInputWidget
from ui.widgets.subject_input_widget import SubjectInputWidget
from ui.widgets.time_input_widget import TimeInputWidget


class UserTextInputPanel(QWidget):
    assignmentNameInput = None
    subjectInput = None
    priorityInput = None

    def __init__(self):
        super().__init__()
        self.assignmentNameInput = AssignmentNameInputWidget()
        self.subjectInput = SubjectInputWidget()
        self.priorityInput = PriorityInputWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.subjectInput)
        layout.addWidget(self.assignmentNameInput)
        layout.addWidget(self.priorityInput)
        self.setLayout(layout)


class UserInputWidget(QWidget):
    textInputPanel = None
    dateInput = None
    timeInput = None

    def __init__(self):
        super().__init__()
        leftLayout = QVBoxLayout()
        self.textInputPanel = UserTextInputPanel()
        self.dateInput = DateInputWidget()
        self.timeInput = TimeInputWidget()
        leftLayout.addWidget(self.textInputPanel)
        leftLayout.addWidget(self.dateInput)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addWidget(self.timeInput)

        self.setLayout(mainLayout)
