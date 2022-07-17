"""
Nick Depatie
Assignment Database GUI
This script will create a QT GUI to allow the user to log assignments to a mySQL database, 
    access the items in the database, and sort the items by urgency using merge sort 
    (i.e. how close the deadline is and how important is the assignment)
"""

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())