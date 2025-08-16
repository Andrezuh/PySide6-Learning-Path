from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QListWidget, QAbstractItemView, QPushButton, QButtonGroup

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QListWidget')

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem('One')
        self.list_widget.addItems(['Two','Three'])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)

        self.setLayout(v_layout)

    def current_item_changed(self, item):
        print(f'Current item: {item.text()}')
    def current_text_changed(self, text):
        print(f'Current text changed: {text}')