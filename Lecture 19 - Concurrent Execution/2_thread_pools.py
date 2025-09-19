from PySide6.QtCore import QTimer, QRunnable, QThreadPool, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QVBoxLayout, QWidget)

import sys
import time

""" We use the same example as last file, but this time we'll delegate the method
functionality to a QRunnable object. This class allows for containing
instructions that require to be run concurrently with others in the app event
loop. It is then combined with a QThreadPool which is a manager of the
available threads in the system. This object executes simultaneous instructions
or queues them if all threads are busy. 

In this example, this configuration
allows the counter to continue uninterrupted while the other instructions execute
"""

class Worker(QRunnable):

    @Slot()
    def run(self):
        print('Thread start')
        time.sleep(5)
        print('Thread complete')

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

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        # A thread pool is initialized to manage all incoming QRunnable objects
        self.threadpool = QThreadPool()
        threads = self.threadpool.maxThreadCount()

        print(f'Multithreading with maximum {threads} threads')

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')

    # Now in this method we create an instance of the QRunnable object, and then
    # assign it to the pool, for it to be auto-destroyed when it finishes
    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
