from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from os import path
import sys

basedir = path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        # In order to connect to a database, a QSqlDatabase instance is to be
        # created. It allows the configuration of the desired SQL
        # file or server, and to open a connection to it.

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(path.join(basedir, 'Chinook_Sqlite.sqlite'))
        db.open()

        # After a successful connection to the database, a model of it has to
        # be created to allow an interface with the table view. At current
        # configuration, only one table can be accessed.

        self.model = QSqlTableModel(db=db)

        self.table.setModel(self.model)

        self.model.setTable('Album')
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()