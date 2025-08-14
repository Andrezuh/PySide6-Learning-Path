from PySide6.QtWidgets import QApplication
import sys
from rockwidget import RockWidget

app = QApplication(sys.argv)
window = RockWidget()
window.show()

app.exec()