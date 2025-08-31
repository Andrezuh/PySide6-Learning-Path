from PySide6.QtWidgets import QApplication
from widget import MainWidget
import sys

app = QApplication(sys.argv)

widget = MainWidget(app)
widget.show()

app.exec()