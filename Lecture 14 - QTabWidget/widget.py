from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit, QSpacerItem

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTabWidget Demo')

        # The process to insert tabs into the QTabWidget is
        # 1) Create the base object and define the parent
        # 2) Each tab will be a QWidget object, so at least one is to be initialized
        # 3) Insert the content into the QWidget object
        # 4) Add each QWidget into the QTabWidget object

        # Step 1: Create the QTabWidget instance with parent
        tab_widget = QTabWidget(self)

        # Steps 2 and 3: Create QWidget objects and populate them with other widgets

        # Tab 1: Information
        widget_form = QWidget()
        label_full_name = QLabel('Full name:')
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

        # Tab 2: Buttons
        widget_buttons = QWidget()
        button_1 = QPushButton('One')
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton('Two')
        button_3 = QPushButton('Three')
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)
        buttons_layout.addWidget(button_2)
        buttons_layout.addWidget(button_3)
        widget_buttons.setLayout(buttons_layout)

        # Step 4: Add each Qwidget as a tab in the base object
        # Use the following method
        # -> QTabWidget.addTab(QWidget, 'Tab Name')

        tab_widget.addTab(widget_form, 'Information')
        tab_widget.addTab(widget_buttons, 'Buttons')

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def button_1_clicked(self):
        print('Button 1 clicked!')
