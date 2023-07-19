"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChat_loginScreen_GUI import Ui_loginScreen_MainWindow
import time


class pyChatClientBackend:
    def __init__(self):
        # Defaults setup
        self.current_datetime = time.ctime()

        # Window setup
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_loginScreen_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.currentDateTime_label.setText(self.current_datetime)

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    client = pyChatClientBackend()
    client.run()
