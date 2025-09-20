from PySide6.QtCore import(QObject, QRunnable, QThreadPool, QTimer, Signal, Slot)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QProgressBar, QVBoxLayout, QWidget)

import sys
import time

"""
This file will show an example of a button which will start a progress
calculation that will be shown with a QProgressBar object. The calculation runs
on a thread, and will update the bar every 0.01 s.
"""

class WorkerSignals(QObject):
    """
    Only the progress signal will be used in the worker, using an int
    """
    progress = Signal(int)


class Worker(QRunnable):
    """ Example """
    def __init__(self):
        """ xample """
        super().__init__()

        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000 # Number of iterations
        progress_pc = 0
        for n in range(total_n):
            progress_pc = int(
                (100 * float(n+1)) / total_n
            ) # Progress percentage calculation
            self.signals.progress.emit(progress_pc)
            time.sleep(0.01)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout = QVBoxLayout()

        self.progressbar = QProgressBar()
        self.button = QPushButton('START IT UP!!!')
        self.button.clicked.connect(self.execute)
        
        layout.addWidget(self.progressbar)
        layout.addWidget(self.button)

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.threadpool = QThreadPool()
        self.maxthreads = self.threadpool.maxThreadCount()
        print(f'Multithreading with maximum {self.maxthreads} threads')

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(worker)

    def update_progress(self, progress:int):
        self.progressbar.setValue(progress)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()