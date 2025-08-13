# Importing the components we need
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

# The sys module is responsible for processing command line arguments.
import sys

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()