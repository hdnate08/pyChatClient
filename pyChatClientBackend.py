"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChat_applicationScreen_GUI import Ui_applicationScreen_MainWindow
from pyChat_loginScreen_GUI import Ui_loginScreen_MainWindow


class pyChatClientBackend:
    def __init__(self):
        # Window setup
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_loginScreen_MainWindow()
        self.ui.setupUi(self.window)

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    client = pyChatClientBackend()
    client.run()
