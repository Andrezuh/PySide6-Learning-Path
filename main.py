# Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# The sys module is responsible for processing command line arguments.
import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

button = QPushButton()
button.setText("Press me")

window.setCentralWidget(button)

window.show()
app.exec()