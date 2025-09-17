# This lecture is following the Concurrent Exectution introduction and tutorial
# from Martin Fitzpatrick in the Python GUI's webpage.
# https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QVBoxLayout, QWidget)

import sys
import time

# In this example we setup a counter shwoing how many seconds have passed inside
# a label, and also a button with a timeout of 5 seconds when pressed. The problem
# with this example lies that when the button is clicked, the counter stops and
# the program freezes while the timeout finishes. This is because the tasks
# are running in the same thread and cannot run simultaneously, only in sequence.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0

        container = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel('Start')
        self.button = QPushButton('DANGER!!!')
        self.button.clicked.connect(self.oh_no)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container.setLayout(layout)

        self.setCentralWidget(container)

        # The QTimer object is an interface for timers with a specified time
        # interval (in miliseconds). In this case the timer fires continuously
        # every second, calling the recurring_timer() method

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    # This is the main method called when 1000 miliseconds have passed, according
    # to the QTimer object
    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')

    # When this method is called, it interrupts recurring_method() and freezes
    # the application while 5 seconds pass in the process
    """ 
    def oh_no(self):
        time.sleep(5)
    """

    # If instead, we setup a event processor inside the oh_no() method, it will
    # allow the event loop to respond to OS events, in this case the continous
    # timer. However, events are now no longer controlled by the code, but by 
    # Qt, making the running tasks longer and with possible undefined behaviour.

    # This is not recommended AT ALL!!!
    def oh_no(self):
        for n in range(5):
            QApplication.processEvents()
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()