from PyQt5.QtWidgets import (
    QWidget, 
    QHBoxLayout,
    QVBoxLayout
    )
from .date_input_widget import DateInputWidget
from .assignment_name_input_widget import AssignmentNameInputWidget
from .priority_input_widget import PriorityInputWidget
from .subject_input_widget import SubjectInputWidget
from .time_input_widget import TimeInputWidget


class UserTextInputPanel(QWidget):
    assignmentNameInput = AssignmentNameInputWidget()
    subjectInput = SubjectInputWidget()
    priorityInput = PriorityInputWidget()

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(self.subjectInput)
        layout.addWidget(self.assignmentNameInput)
        layout.addWidget(self.priorityInput)
        self.setLayout(layout)


class UserInputWidget(QWidget):
    textInputPanel = UserTextInputPanel()
    dateInput = DateInputWidget()
    timeInput = TimeInputWidget()

    def __init__(self):
        super().__init__()
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.textInputPanel)
        leftLayout.addWidget(self.dateInput)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addWidget(self.timeInput)

        self.setLayout(mainLayout)
