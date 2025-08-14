from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
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

    def quit_app(self):
        self.app.quit()