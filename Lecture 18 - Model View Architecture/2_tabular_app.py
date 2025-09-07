from PySide6.QtWidgets import (QWidget, QMainWindow, QApplication, QTableView)
from PySide6.QtCore import QPersistentModelIndex, Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QColor, QIcon
import sys
from datetime import datetime
from os import path

hue = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0',
'#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']

basedir = path.dirname(__file__)

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
    
    """
    def data(self, index:QModelIndex, role):

        # DEMO 1: Value Formatting
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
        
        # Depending on the assigned role, different things can be styled in the
        # cell, like alignment, text color, background color and/or hue, etc.

        # DEMO 2: Text color

        if role == Qt.ItemDataRole.BackgroundRole and index.column() == 2:
            return QColor(Qt.GlobalColor.blue)

        # DEMO 3: Text alignment

        if role == Qt.ItemDataRole.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight

        # DEMO 4: Text colors

        if role == Qt.ItemDataRole.ForegroundRole:
            value = self._data[index.row()][index.column()]

            if (
                isinstance(value, int) or isinstance(value, float)
            ) and value < 0:
                return QColor('red')
  
        # DEMO 5: Color gradient
        if role == Qt.ItemDataRole.BackgroundRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, (int, float)):
                value = int(value)

                value = max(-5, value)
                value = min(5, value)
                value = value + 5

                return QColor(hue[value])
    """       

    # DEMO 6: Cell decoration
    def data(self, index:QModelIndex, role):

        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%d')
            
            return value
        
        elif role == Qt.ItemDataRole.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QIcon(path.join(basedir, 'calendar.png'))
            
            elif isinstance(value, bool):
                if value:
                    return QIcon(path.join(basedir, 'tick.png'))
                else:
                    return QIcon(path.join(basedir, 'cross.png'))
            elif isinstance(value, (int,float)):
                value = int(value)

                value = max(-5, value)
                value = min(5, value)
                value = value + 5

                return QColor(hue[value])
        

    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        # To use in DEMO 1, 2, 3 and 4

        # data = [
        #     [4, 9, 2],
        #     [1, -1, 'hello'],
        #     [3.023, 5, -5],
        #     [3, 3, datetime(2017,10,1)],
        #     [7.555, 8, 9],
        # ]

        # To use in DEMO 5
        # data = [
        #     [4,9,2],
        #     [1,-1,-1],
        #     [3,5,-5],
        #     [3,3,2],
        #     [7,8,9]
        # ]

        # To use in DEMO 6
        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019, 5, 4), 8, 9],
        ]

        self.model = TableModel(data)

        self.table.setModel(self.model)
        
        self.setCentralWidget(self.table)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()