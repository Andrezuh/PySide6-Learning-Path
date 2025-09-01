from PySide6.QtWidgets import (QWidget, QApplication, QGridLayout, QGroupBox,
                               QComboBox, QLabel, QLineEdit, QPushButton,
                               QCheckBox, QPlainTextEdit, QVBoxLayout, 
                               QStyleFactory, QSpinBox)
from PySide6.QtGui import QPalette, QColorConstants, QColor

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

        # Demo 2: Palettes

        # QPalettes are standalone objects or information part of an existing
        # widget, which holds color configuration, including how it is applied
        # to the widget (i.e. text, background, cursor, highlight, etc.)

        colors = ['white','red','green','blue','black','cyan','magenta','yellow',
                  'gray'] # Define basic colors for combobox selection
        
        self.globalPalette = QPalette() # Global palette that contains color config

        group2 = QGroupBox('QPallete')
        group2_layout = QGridLayout()
        group2_textLabel = QLabel('Text')
        group2_backgroundLabel = QLabel('Background')
        self.group2_textCombo = QComboBox(editable=False,
                                          placeholderText='Select a color')
        self.group2_textCombo.addItems(colors)
        self.group2_backgroundCombo = QComboBox(editable=False,
                                                placeholderText='Select a color')
        self.group2_backgroundCombo.addItems(colors)
        self.group2_testLabel = QLabel('This is some text')
        self.group2_testLabel.setAutoFillBackground(True)
        group2_layout.addWidget(group2_textLabel, 0,0)
        group2_layout.addWidget(group2_backgroundLabel, 0,1)
        group2_layout.addWidget(self.group2_textCombo, 1,0)
        group2_layout.addWidget(self.group2_backgroundCombo, 1,1)
        group2_layout.addWidget(self.group2_testLabel, 2,0, 1,2)
        group2.setLayout(group2_layout)

        self.group2_textCombo.currentTextChanged.connect(self.change_text_color)
        self.group2_backgroundCombo.currentTextChanged.connect(self.change_background_color)

        # Demo 3: StyleSheets

        # While QPalette is a great tool for configuring color, it isn't able
        # to change other visual properties of a widget, for example text size,
        # width, height, border type, etc. This is where StyleSheets come in.
        # In essence, they are instructions on how a specific widget will look
        # like. For this, it uses a similar structure to CSS to set every
        # parameter needed, like this

        """
        Widget {
            parameter1 : value;
            parameter2 : value;
            ...
        }
        """

        # Visual properties mostly follow the CSS standard properties, but the
        # official supported ones are listed in the PySide6 documentation:
        # https://doc.qt.io/qtforpython-6/overviews/qtgui-richtext-html-subset.html#css-properties

        self.group3 = QGroupBox('Styling Sheets')
        group3_layout = QVBoxLayout()
        self.group3_textEdit = QPlainTextEdit()
        self.group3_checkbox = QCheckBox('Checkbox')
        self.group3_comboBox = QComboBox(editable=False, placeholderText='Selectable')
        self.group3_spinBox = QSpinBox(minimum=0, maximum=100, value=0)
        self.group3_label = QLabel('Text')
        self.group3_lineEdit = QLineEdit(placeholderText='This is a text')
        self.group3_button = QPushButton('Button')
        group3_layout.addWidget(self.group3_textEdit)
        group3_layout.addWidget(self.group3_checkbox)
        group3_layout.addWidget(self.group3_comboBox)
        group3_layout.addWidget(self.group3_spinBox)
        group3_layout.addWidget(self.group3_label)
        group3_layout.addWidget(self.group3_lineEdit)
        group3_layout.addWidget(self.group3_button)
        self.group3.setLayout(group3_layout)

        self.group3_textEdit.textChanged.connect(self.set_style_sheet)

        mainLayout.addWidget(group1, 0,0)
        mainLayout.addWidget(group2, 1,0)
        mainLayout.addWidget(self.group3, 0,1, 2,1)

        self.setLayout(mainLayout)

    def change_window_style(self, style):
        self.app.setStyle(style)

    def change_text_color(self, color):
        self.globalPalette.setColor(QPalette.ColorRole.WindowText, QColor.fromString(color))
        self.group2_testLabel.setPalette(self.globalPalette)

    def change_background_color(self, color):
        self.globalPalette.setColor(QPalette.ColorRole.Window, QColor.fromString(color))
        self.group2_testLabel.setPalette(self.globalPalette)

    def set_style_sheet(self):
        qss = self.group3_textEdit.toPlainText()
        # The Qt engine will automatically parse the style sheet, and apply
        # the changes if it's valid.
        self.group3.setStyleSheet(qss)

        
