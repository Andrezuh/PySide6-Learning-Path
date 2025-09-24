from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                               QPushButton, QSpinBox, QVBoxLayout)
import sys
import time

"""
So far, to use concurrency in our application, we have been using a thread-pool
architecture. This approach is limited by the worker activation by the user, and
the maximum number of orders that the pool can handle at a time. But with long
running, or permanent tasks, this configuration is not optimal. 

In this case, there is wrapper called 'QThread' which, as a derivate of a QObject, 
can handle thread concurrency, signal assignment in the same object, and state 
control methods. As well as QRunnable, it maintains a separate thread from the
GUI, preventing blocking its work (even when signals are emitted!).

"""

class Worker(QThread):
    """
    Apart from specifying the executing code in the run() method, we also set up
    a flag to stop the thread internally (and avoid crashing the app), and a
    public method to send data to the thread, via external functions or classes.
    """

    # Signal assignment to thread object
    result = Signal(str)

    @Slot()
    def run(self):
        self.data = None
        self.is_running = True # Termination flag

        print('Thread start')
        counter = 0

        while True:
            # Waiting loop (keep the thread alive whilst no data is read)
            while self.data is None:
                if not self.is_running:
                    return
                time.sleep(0.1)

            counter += self.data
            self.result.emit(f'The number is {counter}')
            self.data = None

    # Data receiver method
    def send_data(self, data:int):
        self.data = data

    # Method to change termination flag
    def stop(self):
        self.is_running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout = QVBoxLayout()

        self.worker = Worker()
        self.worker.start() # A QThread object can be started without a pool

        self.spinbox = QSpinBox(minimum=0, singleStep=1)
        self.submit_button = QPushButton('Submit number')
        self.label = QLabel('Output will appear here')
        self.kill_button = QPushButton('Kill thread')

        self.submit_button.clicked.connect(self.submit_data)
        
        
        """
        While it's possible to use the .terminate() method of the worker thread,
        it is not recommended if the program wants to retrieve the object status
        in a later stage, because the thread wasn't finished 'cleanly' and will
        crash the program. For that reason, at least in this case, a termination
        flag inside the thread execution is preferred.
        """
        # self.kill_button.clicked.connect(self.worker.terminate)
        self.kill_button.clicked.connect(self.worker.stop)
        self.worker.result.connect(self.label.setText)
        self.worker.finished.connect(self.thread_has_finished)

        layout.addWidget(self.spinbox)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.label)
        layout.addWidget(self.kill_button)

        container.setLayout(layout)

        self.setCentralWidget(container)

    # Get value and send it to the thread worker
    def submit_data(self):
        value = self.spinbox.value()
        self.worker.send_data(value)    

    def thread_has_finished(self):
        print('Thread has finished.')
        print(
            self.worker,
            self.worker.isRunning(),
            self.worker.isFinished()
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
