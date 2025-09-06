from PySide6.QtWidgets import (QWidget, QMainWindow, QApplication, QTableView)
from PySide6.QtCore import QPersistentModelIndex, Qt, QAbstractTableModel, QModelIndex
import sys

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index:QModelIndex, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            [4,1,3,3,7],
            [9,1,5,3,8],
            [2,1,5,3,9]
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)
        
        self.setCentralWidget(self.table)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()