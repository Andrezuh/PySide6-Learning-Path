from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QMessageBox')

        button_hard = QPushButton('Hard')
        button_hard.clicked.connect(self.button_clicked_hard)
        
        button_critical = QPushButton('Critical')
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton('Question')
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton('Information')
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton('Warning')
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton('About')
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    # The 'hard way' of showing a message box
    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle('Message Title')
        message.setText('Something happened')
        message.setInformativeText('Do you want to do something about it?')
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print('User chose OK')
        else:
            print('User chose Cancel')

    def button_clicked_critical(self):
        print('Critical')

    def button_clicked_question(self):
        print('Question')

    def button_clicked_information(self):
        print('Information')

    def button_clicked_warning(self):
        print('Warning')

    def button_clicked_about(self):
        print('About')