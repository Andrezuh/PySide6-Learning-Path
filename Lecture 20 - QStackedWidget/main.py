from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                               QPushButton,QStackedWidget, QVBoxLayout)
import sys

"""
An application sometimes uses different widgets to display information and
interact with the user in different ways. However, a series of top-level widgets
cannot be shown at once, only with a dedicated type of widget that holds them.
The first example was shown in Lecture 14 with the QTabWidget object, displaying
all inserted widgets and changed between them with the tab system.

Another way to handle multiple widgets is with the QStackedWidget object. It
allows for indexing multiple widgets in an internal list, and exclusively within
the code, change between them using the desired index, or with the widget object
reference. All of this within a single application window.

In this example there will be 2 widget objects inserted into the QStackedWidget
object, and changed with buttons set up in each one.
"""

class Widget1(QWidget):
    def __init__(self, app):
        """
        In order to interact with the QStackedWidget object, we pass the
        MainWindow class as an __init__ argument, and perform the desired code
        """
        super().__init__()

        self.app = app # Define the argument as a class instance

        layout = QVBoxLayout()

        label = QLabel('This is widget 1')
        button = QPushButton('Push for widget 2')
        button.clicked.connect(self.change_widget)

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

    def change_widget(self):
        self.app.stackedWidget.setCurrentIndex(1) # Change displayed widget
        print('Changed to widget with index 1')

class Widget2(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app

        layout = QVBoxLayout()

        label = QLabel('This is widget 2')
        button = QPushButton('Push for widget 1')
        button.clicked.connect(self.change_widget)

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)


    def change_widget(self):
        self.app.stackedWidget.setCurrentIndex(0)
        print('Changed to widget with index 0')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget1 = Widget1(self)
        self.widget2 = Widget2(self)

        """  
        Similar to QTabWidget, all widgets are added to the "container" and
        retrieved via index or object reference
        """
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.widget1)
        self.stackedWidget.addWidget(self.widget2)

        self.setCentralWidget(self.stackedWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()