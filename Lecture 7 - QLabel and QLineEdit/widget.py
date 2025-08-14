from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel and QLineEdit')

        # A set of signals we can connect to
        label = QLabel('Fullname: ')
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)

        button = QPushButton('Grab data')
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel('I Am Here')

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    # Slots
    def button_clicked(self):
        print(f'Fullname: {self.line_edit.text()}')
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        print(f'Text changed to: {self.line_edit.text()}')
        self.text_holder_label.setText(self.line_edit.text())
