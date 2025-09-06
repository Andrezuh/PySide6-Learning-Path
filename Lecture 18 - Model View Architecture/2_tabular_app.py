from PySide6.QtWidgets import (QWidget, QMainWindow, QApplication, QTableView)
from PySide6.QtCore import QPersistentModelIndex, Qt, QAbstractTableModel, QModelIndex
import sys
from datetime import datetime

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # DEMO 1: Value Formatting
    def data(self, index:QModelIndex, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value =  self._data[index.row()][index.column()]

            # By default, the values are formatted either as a float, int, or
            # bool. If any more format types are to be recognized, a manual
            # configuration (like the one below) is to be made.

            if isinstance(value, str): # String renderer
                return f'{value}'
            elif isinstance (value, float): # Float of 2 decimal points renderer
                return f'{value:.2f}'
            elif isinstance(value, datetime): # YYYY-MM-DD date renderer
                return value.strftime('%Y-%m-%d')
            else:
                # If value is in another non-recognized format, it just
                # returns the value
                return value
        
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        # To use in DEMO 1
        data = [
            [4, 9, 2],
            [1, -1, 'hello'],
            [3.023, 5, -5],
            [3, 3, datetime(2017,10,1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)
        
        self.setCentralWidget(self.table)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()