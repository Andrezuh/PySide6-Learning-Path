from PySide6.QtSql import (QSqlRelationalTableModel, QSqlRelation, QSqlDatabase,
                           QSqlRelationalDelegate, QSqlQuery)
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableView)
from PySide6.QtCore import Qt, QSize
from os import path
import sys

basedir = path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName(path.join(basedir, 'Chinook_Sqlite.sqlite'))
        db.open()

        # When a table wants to be shown, but a column is related to another in
        # a different table, then a relational database is needed. With this
        # object, relations between columns can be established
        
        self.model = QSqlRelationalTableModel(db=db)

        self.table = QTableView()

        self.table.setModel(self.model)
        self.model.setTable('Track')

        # A relation can be established like this

        # model.setRelation(<table_column>, QSqlRelation(<foreign_table>, 
        # <foreign_key>, <foreign_column>))

        """ 
        self.model.setRelation(
            2, QSqlRelation('Album','AlbumId','Title')
        )
        self.model.setRelation(
            2, QSqlRelation('Album','AlbumId','Title')
        )
        self.model.setRelation(
            3, QSqlRelation('MediaType','MediaTypeId','Name')
        )
        self.model.setRelation(
            4, QSqlRelation('Genre','GenreId','Name')
        )
        """

        # A delegate allows for editing a cell looking up the values in the
        # related column, with a display of the options in a combo box
        """
        self.delegate = QSqlRelationalDelegate(self.table)
        self.table.setItemDelegate(self.delegate)
        """

        self.model.select()

        self.setMinimumSize(1024,800)
        self.setCentralWidget(self.table)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()