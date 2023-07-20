"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QTime, QDate
from pyChat_loginScreen_GUI import Ui_loginScreen_MainWindow
from pyChatClient import PyChatClient
import time


class pyChatClientBackend:
    def __init__(self):
        # Window setup
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_loginScreen_MainWindow()
        self.ui.setupUi(self.window)

        # Connecting buttons to their respective functions
        self.ui.login_pushButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.ui.forgotPasswordButton.clicked.connect(self.passwordReset)
        self.ui.exitButton.clicked.connect(self.exit)

        # Defaults setup
        self.pychat_client = PyChatClient('127.0.0.7', 60002, self.ui.connectionStatusLabel)
        self.clock = QTimer(self.window)

        # Default settings
        self.window.closeEvent = self.close_event
        self.ui.username_lineEdit.setPlaceholderText('Username')
        self.ui.password_lineEdit.setPlaceholderText('Password')
        # Update the clock label every second
        self.clock.timeout.connect(self.update_clock)
        self.clock.start(1000)

        # Connection setup
        self.pychat_client.connect()

    def update_clock(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        # Format time and date
        time_text = current_time.toString("hh:mm:ss AP")  # 12-hour format with AM/PM
        date_text = current_date.toString("dddd, MMMM d, yyyy")  # e.g., Monday, July 1, 2023

        # Combine time and date
        datetime_text = f"{date_text}  {time_text}"
        self.ui.currentDateTime_label.setText(datetime_text)

    def login(self):
        print("Inside of login")

    def register(self):
        print("Inside of register")

    def passwordReset(self):
        print("Inside of passwordReset")

    def exit(self):
        print("Inside of exit")

    def close_event(self, event):
        self.pychat_client.close()
        event.accept()

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    client = pyChatClientBackend()
    client.run()
