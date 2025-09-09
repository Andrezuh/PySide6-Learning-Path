from PySide6.QtWidgets import (QApplication, QMainWindow, QTableView,
                               QLineEdit, QWidget, QVBoxLayout)
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from os import path
import sys

basedir = path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout = QVBoxLayout()

        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)

        self.table = QTableView()

        layout.addWidget(self.search)
        layout.addWidget(self.table)
        container.setLayout(layout)

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

        # The table, and the database, is editable by default by the user in
        # the view. To change  the behaviour, Qt allows for strategy config

        """ self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit) """

        self.model.setTable('Track')

        # Sorting columns
        """ self.model.setSort(2, Qt.SortOrder.DescendingOrder) # Sort column 3 """

        # Sorting columns with field index
        """ idx = self.model.fieldIndex('Miliseconds') # Column lookup
        self.model.setSort(idx, Qt.SortOrder.DescendingOrder) """

        # Setting column titles in view
        """ 
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, 'Name')
        self.model.setHeaderData(2, Qt.Orientation.Horizontal, 'Album (ID)')
        self.model.setHeaderData(3, Qt.Orientation.Horizontal, 'Media Type (ID)')
        self.model.setHeaderData(4, Qt.Orientation.Horizontal, 'Genre (ID)')
        self.model.setHeaderData(5, Qt.Orientation.Horizontal, 'Composer')
        """
        # Column titles with a dictionary
        """ 
        column_titles = {
            'Name': 'Name',
            'AlbumId': 'Album (ID)',
            'MediaTypeId': 'Media Type (ID)',
            'GenreId': 'Genre (ID)',
            'Composer': 'Composer'
        }

        for key, value in column_titles.items():
            idx = self.model.fieldIndex(key)
            self.model.setHeaderData(idx, Qt.Orientation.Horizontal, value)
        """

        # Removing columns (only from view)
        """ self.model.removeColumns(2,5) """

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(container)

    def update_filter(self, s):
        filter_str = f'Name LIKE "%{s}%"' # Uses an SQL WHERE clause
        self.model.setFilter(filter_str)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()