from PySide6.QtCore import (QTimer, QRunnable, QThreadPool, Signal, Slot, 
                            QObject)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QVBoxLayout, QWidget)

import sys
import time
import random as rd

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

"""
While a worker is designed primarily to execute an instruction, sometimes it's
necessary to tranfer data or state information between the worker and the GUI
application. For that, there lies the possibility to create and customize signals
and slots (within a QObject) and safely exchange information while the worker
runs on a thread.
"""

# This class is responsible for holding all possible signals that can be assigned
# to the QRunnable worker. Each one will be configured for a different outcome
# and with different input parameters.
class WorkerSignals(QObject):
    
    finished = Signal()
    error = Signal(str)
    result = Signal(dict)

# For this example, there is a calculation with a number of interations,
# which can result in a zero-division. We initialize the worker signals object
# and configure the singal emmisions within the try-except block in the run()
# method. This will show both possible cases of calculation and log the result
# in the terminal.
class Worker2(QRunnable):
    def __init__(self, iterations=5):
        super().__init__()
        self.signals = (WorkerSignals())
        self.iterations = iterations
    
    @Slot()
    def run(self):
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40-n)
        except Exception as e:
            # When an error is raised, the signal will emit the exception as a
            # string
            self.signals.error.emit(str(e))
        else:
            # When a successful calculation is made, it will emit the finished
            # signal, and the result signal with a dict with values.
            self.signals.finished.emit()
            self.signals.result.emit({'n':n, 'value':v})

# While maintaining the concurrent timer, we will setup and configure the signal
# functionality for when the button is clicked and the calculations are queued
# in the thread pool.
class MainWindow2(QMainWindow):
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

        self.threadpool = QThreadPool()
        max_threads = self.threadpool.maxThreadCount()
        print(f'Multithreading with maximum {max_threads} threads')

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        worker = Worker2(iterations=rd.randint(10,50))
        # Tie each slot with a defined signal functionality in the class
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)
    
    def worker_output(self,s):
        print('Result', s)

    def worker_complete(self):
        print('Thread complete')

    def worker_error(self, t):
        print(f'Error: {t}')
    
    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = MainWindow()
    # window.show()

    window2 = MainWindow2()
    window2.show()
    app.exec()
