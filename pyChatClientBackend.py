"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChatClient import PyChatClient
from pyChat_loginScreen_GUI import Ui_loginScreen_MainWindow
import config
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
        self.is_connected = False
        self.pychat_client = PyChatClient(config.DEFAULT_IP, config.DEFAULT_PORT)
        self.clock_timer = QTimer(self.window)
        self.connection_timer = QTimer(self.window)

        # Default settings
        self.window.closeEvent = self.close_event
        self.ui.username_lineEdit.setPlaceholderText('Username')
        self.ui.password_lineEdit.setPlaceholderText('Password')

        # Timers
        self.clock_timer.timeout.connect(self.clock_updater)
        self.clock_timer.start(config.CLOCK_TIMER_INTERVAL)
        self.connection_timer.timeout.connect(self.connect_to_server)
        self.connection_timer.start(config.CONNECTION_RETRY_INTERVAL)

#TODO: Implement check_connection() function which runs connect_to_server() if necessary
    def connect_to_server(self):
        if not self.is_connected:
            self.is_connected = self.pychat_client.connect()
            if self.is_connected:
                self.ui.connectionStatusLabel.setText("Connected")
            else:
                self.ui.connectionStatusLabel.setText("Connection failed. Retrying...")

    # Function for updating widgets (1000ms)
    def clock_updater(self):
        # Update GUI clock
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        time_text = current_time.toString("hh:mm:ss AP")  # 12-hour format with AM/PM
        date_text = current_date.toString("dddd, MMMM d, yyyy")  # e.g., Monday, July 1, 2023
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
