from PySide6.QtCore import(QObject, QRunnable, QThreadPool, QTimer, Signal, Slot)
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QProgressBar, QVBoxLayout, QWidget)

import sys
import time
import uuid
import random

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
        super().__init__()

        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000 # Number of iterations or steps
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

""" 
Although the update of the progress is being rendered correctly in the progress
bar, when multiple calculations or threads are initialized the bar tries to
show all values it receives, so it looks that it's jumping back and foward
between values. Tracking the progress of multiple workers is possible, and in
this case we will average the running workers progress, to show a single number.

To do this, we will use unique identifiers for each worker, and store their
values in the application.
"""

class WorkerSignals2(QObject):
    progress = Signal(str, int)
    finished = Signal(str)

class Worker2(QRunnable):
    def __init__(self):
        super().__init__()

        self.jod_id = uuid.uuid4().hex # Create the unique identifier
        self.signals = WorkerSignals2()

    @Slot()
    def run(self):
        total_n = 1000 # Number of iterations or steps
        delay = random.random() / 100 # Random delay value
        progress_pc = 0
        for n in range(total_n):
            progress_pc = int(100 * float(n+1) / total_n)
            self.signals.progress.emit(self.jod_id, progress_pc)
            time.sleep(delay)
        
        self.signals.finished.emit(self.jod_id)

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker_progress = {} # Dict to hold all active workers

        container = QWidget()
        layout = QVBoxLayout()

        self.progressbar = QProgressBar()
        self.button = QPushButton('START IT UP!!!')
        self.button.clicked.connect(self.execute)
        self.status = QLabel('0 workers')
        
        layout.addWidget(self.progressbar)
        layout.addWidget(self.button)
        layout.addWidget(self.status)

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.threadpool = QThreadPool()
        self.maxthreads = self.threadpool.maxThreadCount()
        print(f'Multithreading with maximum {self.maxthreads} threads')

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refresh_progress)
        self.timer.start()

    def execute(self):
        worker = Worker2()
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finished.connect(self.cleanup)

        self.threadpool.start(worker)

    def cleanup(self, job_id):
        """
        Refresh the progress percentage and delete worker record if finished
        """
        if job_id in self.worker_progress:
            del self.worker_progress[job_id]
        
        self.refresh_progress()

    def update_progress(self, job_id:str, progress:int):
        """
        Update the record in the worker dictionary
        """
        self.worker_progress[job_id] = progress

    def calculate_progress(self):
        """
        Average all active workers progress, or return 0 if none are active
        in the pool
        """
        if not self.worker_progress:
            return 0
        
        return int(
            sum(v for v in self.worker_progress.values()) / len(self.worker_progress)
        )
    
    def refresh_progress(self):
        """
        Get the average progress and update the value in the progress bar and
        the label
        """
        progress = self.calculate_progress()
        print(self.worker_progress)
        self.progressbar.setValue(progress)
        self.status.setText(f'{len(self.worker_progress)} workers')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = MainWindow()
    # window.show()

    window2 = MainWindow2()
    window2.show()
    app.exec()