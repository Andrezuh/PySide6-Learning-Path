from PySide6.QtCore import (QObject, QRunnable, QSize, QThreadPool, QTimer, Qt, Signal,
                            Slot)
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QPushButton,
                               QVBoxLayout)

import pyqtgraph as pg

import sys
import time
import uuid
import random

"""
In order to perfom multiple updates on a GUI while performing background
calculations, multithreading may be the best choice to allow the application
to function while the threads are active. In this example it will be shown how
a worker performs a calculation based on a current value, and then plots its
result in a GUI plot window with the help of the 'pyqtgraph' library.
"""

class WorkerSignals(QObject):
    """
    The signal will emit a tuple containing the worker id, the x and y positions
    """

    data = Signal(tuple)

class Worker(QRunnable):
    def __init__(self):
        super().__init__()

        self.worker_id = uuid.uuid4().hex # Create unique ID of the worker
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000 # Number of iterations
        y2 = random.randint(0, 10)
        delay = random.random() / 100
        value = 0

        for n in range(total_n):
            y = random.randint(0, 10)
            value += (n * y2) - (n * y)

            self.signals.data.emit((self.worker_id, n, value))
            time.sleep(delay)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # These dictionaries will hold the x, y values, and the plot widget data,
        # respectively
        self.x_values = {}
        self.y_values = {}
        self.lines = {}

        container = QWidget()
        layout = QVBoxLayout()

        self.graphWidget = pg.PlotWidget() # Plot object
        self.graphWidget.setBackground('w')
        
        self.button = QPushButton('Create New Worker')
        self.button.clicked.connect(self.execute)

        layout.addWidget(self.graphWidget)
        layout.addWidget(self.button)

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.threadpool = QThreadPool()

    def execute(self):
        worker = Worker()
        worker.signals.data.connect(self.receive_data)

        self.threadpool.start(worker)

    def receive_data(self, data:tuple[str, int, int]):
        """
        This method unpacks the data received from the signal, checks and creates
        if the worker id exists in the dictionary, and updates the nex x,y values
        and plots them in the widget.
        """
        worker_id, x, y = data

        if worker_id not in self.lines:
            self.x_values[worker_id] = [x]
            self.y_values[worker_id] = [y]

            pen = pg.mkPen(
                width = 2,
                color = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)
                )
            )
            self.lines[worker_id] = self.graphWidget.plot(
                self.x_values[worker_id], self.y_values[worker_id], pen=pen
            )
            return
        
        self.x_values[worker_id].append(x)
        self.y_values[worker_id].append(y)

        self.lines[worker_id].setData(
            self.x_values[worker_id], self.y_values[worker_id]
        ) # .setData() gets the list of points and plots them in the widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()