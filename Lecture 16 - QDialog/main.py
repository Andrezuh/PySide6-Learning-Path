from PySide6.QtWidgets import QApplication
from widget import MainWidget
import sys

app = QApplication(sys.argv)

widget = MainWidget()
widget.show()

app.exec()