from PySide6.QtWidgets import (QWidget, QApplication, QGridLayout, QGroupBox,
                               QComboBox, QLabel, QLineEdit, QPushButton,
                               QCheckBox, QTextEdit, QVBoxLayout, QStyleFactory)
from PySide6.QtGui import QPalette

# This lecture will show how styling works in both the whole application and to
# specific widgets, with Qt in-built methods, and also external styling.

class MainWidget(QWidget):
    # To change the style for the whole application, we pass it as an argument
    def __init__(self, app: QApplication): 
        super().__init__()

        self.app = app

        mainLayout = QGridLayout()

        # Demo 1: Main Window Styling

        # Depending on the OS the application is running, there are default
        # styles for the window to be customized. In this demo, the combobox
        # selection will change the window style, which affects how the widgets
        # look.

        group1 = QGroupBox('Application Styles')
        group1_layout = QVBoxLayout()
        self.styleSelector = QComboBox(editable=False,
                                       placeholderText='Select a style')
        # QStyleFactory.keys() get the available OS style options
        self.styleSelector.addItems(QStyleFactory.keys())
        group1_layout.addWidget(self.styleSelector)
        group1.setLayout(group1_layout)

        self.styleSelector.currentTextChanged.connect(self.change_window_style)

        mainLayout.addWidget(group1, 0,0)

        self.setLayout(mainLayout)

    def change_window_style(self, style):
        self.app.setStyle(style)

        
