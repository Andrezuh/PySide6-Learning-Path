# Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# The sys module is responsible for processing command line arguments.
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")

        # Set up the button as our central widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()