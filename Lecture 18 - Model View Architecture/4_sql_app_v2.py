from PySide6.QtSql import (QSqlRelationalTableModel, QSqlRelation, QSqlDatabase,
                           QSqlRelationalDelegate, QSqlQueryModel, QSqlQuery)
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableView, QLineEdit,
                               QLabel, QVBoxLayout, QHBoxLayout, QWidget)
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

        self.table = QTableView()

        # When a table wants to be shown, but a column is related to another in
        # a different table, then a relational database is needed. With this
        # object, relations between columns can be established
        
        """
        self.model = QSqlRelationalTableModel(db=db)
        self.table.setModel(self.model)
        self.model.setTable('Track')
        """

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
        self.model.select()
        """

        # A delegate allows for editing a cell looking up the values in the
        # related column, with a display of the options in a combo box
        """
        self.delegate = QSqlRelationalDelegate(self.table)
        self.table.setItemDelegate(self.delegate)
        """

        # While the Qt methods for accessing tables is good for simple operations,
        # when a more complex query wants to be made, the QSqlQueryModel object 
        # allows for more flexibility at input.

        self.model = QSqlQueryModel()
        self.table.setModel(self.model)

        """ 
        query = 'SELECT Name, Composer FROM Track'
        self.model.setQuery(QSqlQuery(query, db=db))
        """

        # More complex queries involving joins and parametrized queries can be
        # made. First the object prepares the query, it binds values if 
        # necessary, and it then executes it.

        query = QSqlQuery(db=db)
        query.prepare(
            """
            SELECT Name, Composer, Album.Title FROM Track
            INNER JOIN Album ON Track.AlbumId = Album.AlbumId
            WHERE Album.Title LIKE CONCAT('%',:album_title,'%')
            """
        )
        query.bindValue(':album_title', 'Sinatra')
        query.exec()
        self.model.setQuery(query)

        self.setMinimumSize(1024,800)
        self.setCentralWidget(self.table)

class QueryExample1(QMainWindow):
    def __init__(self):
        super().__init__()

        # GUI
        container = QWidget()
        mainLayout = QVBoxLayout()

        hLayout = QHBoxLayout()

        self.track = QLineEdit(placeholderText='Track name...')
        self.composer = QLineEdit(placeholderText='Artist name...')
        self.album = QLineEdit(placeholderText='Album name...')

        self.track.textChanged.connect(self.update_query)
        self.composer.textChanged.connect(self.update_query)
        self.album.textChanged.connect(self.update_query)

        hLayout.addWidget(self.track)
        hLayout.addWidget(self.composer)
        hLayout.addWidget(self.album)

        self.table = QTableView()

        mainLayout.addLayout(hLayout)
        mainLayout.addWidget(self.table)

        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        # Database and model configuration
        self.db = QSqlDatabase('QSQLITE')
        self.db.setDatabaseName(path.join(basedir, 'Chinook_Sqlite.sqlite'))
        self.db.open()

        self.model = QSqlQueryModel()
        self.table.setModel(self.model)

        self.query = QSqlQuery(db=self.db)
        self.query.prepare(
            """
            SELECT Name, Composer, Album.Title FROM Track
            INNER JOIN Album USING(AlbumId)
            WHERE Track.Name LIKE CONCAT('%',:track_name,'%')
            AND Track.Composer LIKE CONCAT('%',:track_composer,'%')
            AND Album.Title LIKE CONCAT('%',:album_title,'%')
            """
        )

        self.update_query()

    def update_query(self, s=None):
        trackName = self.track.text()
        trackComposer = self.composer.text()
        albumTitle = self.album.text()

        self.query.bindValue(':track_name',trackName)
        self.query.bindValue(':track_composer',trackComposer)
        self.query.bindValue(':album_title',albumTitle)

        self.query.exec()
        self.model.setQuery(self.query)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    query_ex1 = QueryExample1()
    query_ex1.show()
    app.exec()