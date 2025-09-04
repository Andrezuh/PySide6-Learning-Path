# This lecture is following the Model View Architecture introduction and tutorial
# from Martin Fitzpatrick in the Python GUI's webpage.
# https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/

from PySide6.QtWidgets import (QMainWindow, QWidget, QListView, QLineEdit,
                               QPushButton, QVBoxLayout, QHBoxLayout, 
                               QAbstractItemView, QApplication)
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtGui import QImage
import sys
import os

# In software applications, there is a type of architecture pattern called
# 'Model-View-Controller', which separates the logic for data into 3 elements:
# - Model: The representation and/or storage of data
# - View: The interface that presents and recieves data from user
# - Controller: Commnads that interconnect the 'view' and the 'controller'

# In the case of the Qt framework, the controller portion is embedded into the
# view, so for that reason the architecture for its apps is the
# Model/View Architecture.

# First, we start by creating the model logic with the QAbstractListModel, which
# will hold

basedir  = os.path.dirname(__file__)
tick = QImage(os.path.join(basedir, 'tick.png'))

class ToDoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    # It returns the data, either being the task text or the checked icon
    def data(self, index, role):
        status, text = self.todos[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return text
        elif role ==  Qt.ItemDataRole.DecorationRole:
            if status:
                return tick
    
    # it provides the number of available rows to the view
    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI Elements
        self.widget = QWidget()
        self.mainLayout = QVBoxLayout()

        self.todoList = QListView()
        self.todoList.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.todoList.
        self.twoButtons = QHBoxLayout()
        self.completeButton = QPushButton('Complete task')
        self.deleteButton = QPushButton('Delete task')
        self.twoButtons.addWidget(self.completeButton)
        self.twoButtons.addWidget(self.deleteButton)
        self.itemEdit = QLineEdit()
        self.addButton = QPushButton('Add task')

        self.mainLayout.addWidget(self.todoList)
        self.mainLayout.addLayout(self.twoButtons)
        self.mainLayout.addWidget(self.itemEdit)
        self.mainLayout.addWidget(self.addButton)

        self.widget.setLayout(self.mainLayout)

        self.setCentralWidget(self.widget)
        
        # Create instance of the model object, and assign it to the view
        self.model = ToDoModel()
        self.todoList.setModel(self.model)

        self.addButton.clicked.connect(self.add_task)
        self.deleteButton.clicked.connect(self.delete_task)
        self.completeButton.clicked.connect(self.complete_task)

    def add_task(self):
        text = self.itemEdit.text().strip()
        if text:
            self.model.todos.append((False, text)) # Add data to model
            self.model.layoutChanged.emit() # Trigger a refresh of the view
            self.itemEdit.setText('')
    
    def delete_task(self):
        indexes = self.todoList.selectedIndexes()
        
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()] # Delete the data from the model
            self.model.layoutChanged.emit() # Trigger a refresh of the view
            self.todoList.clearSelection()

    def complete_task(self):
        indexes = self.todoList.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()

            state, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # Send a signal to the model telling the data has changed
            self.model.dataChanged.emit(index, index)
            self.todoList.clearSelection()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

