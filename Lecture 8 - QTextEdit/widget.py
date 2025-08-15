from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()

        # The QTextEdit object has in-built methods for text editing
        copy_button = QPushButton('Copy')
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton('Cut')
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton('Paste')
        # paste_button.clicked.connect(self.paste) # In this case, we will use a custom slot

        undo_button = QPushButton('Undo')
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton('Redo')
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton('Set Plain text')
        # set_plain_text_button.clicked.connect(self.set_plain_text) # Custom method

        set_html_button = QPushButton('Set html')
        # set_html_button.clicked.connect(self.set_html) # Custom method

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.text_edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)
