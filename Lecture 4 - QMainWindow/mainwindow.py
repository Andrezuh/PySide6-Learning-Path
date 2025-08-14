from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.setWindowTitle('Custom MainWindow')

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction('Copy')
        edit_menu.addAction('Cut')
        edit_menu.addAction('Paste')
        edit_menu.addAction('Undo')
        edit_menu.addAction('Redo')

        #More menu options
        menu_bar.addMenu('Window')
        menu_bar.addMenu('Settings')
        menu_bar.addMenu('Help')

        # Working with toolbars
        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction('Some action', self)
        action1.setStatusTip('Stutus message for some action')
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon(r".\start.png"), 'Some other action', self)
        action2.setStatusTip('Status message fot some other action')
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton('Click here'))

        # Working with status bar
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        self.statusBar().showMessage('Message from my app', 3000)

    def button1_clicked(self):
        print('Clicked on the button')