from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QComboBox, 
                               QPushButton, QLabel, QLineEdit, QGroupBox,
                               QDialog, QSpacerItem, QSizePolicy as QSP,
                               QDialogButtonBox, QFileDialog, QFontDialog,
                               QColorDialog, QInputDialog)
from PySide6.QtGui import QPalette

# A QDialog object is a top level window generally purposed for
# short term tasks and basic interactions with the user.
# This app will demonstrate the QDialog base class, some of
# its inherited classes, and basic functionality within a single
# widget window.

# The main widget contains the buttons to invoke the Qdialog windows,
# labels and other widgets to show property anb data transfer
# between classes

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()

        # Demo 1: QDialog
        dialog1 = QGroupBox(title='QDialog')
        dialog1_layout = QVBoxLayout()
        dialog1_button = QPushButton('Press me')
        self.dialog1_positionLabel = QLabel('Position:')
        self.dialog1_osLabel  = QLabel('Favorite OS:')
        dialog1_layout.addWidget(dialog1_button)
        dialog1_layout.addWidget(self.dialog1_positionLabel)
        dialog1_layout.addWidget(self.dialog1_osLabel)
        dialog1.setLayout(dialog1_layout)

        self.Dialog1 = Dialog()
        dialog1_button.clicked.connect(self.dialog1_button_pressed)

        # Demo 2: QDialogButtonBox
        dialog2 = QGroupBox(title='QDialogButtonBox')
        dialog2_layout = QVBoxLayout()
        dialog2_button = QPushButton('Press me for buttons')
        self.dialog2_label = QLabel('Some text')
        dialog2_layout.addWidget(dialog2_button)
        dialog2_layout.addWidget(self.dialog2_label)
        dialog2.setLayout(dialog2_layout)

        self.Dialog2 = ButtonsDialog()
        dialog2_button.clicked.connect(self.dialog2_button_pressed)

        # Demo 3: QFileDialog

        # QFileDialog is a window that allows the user to browse file directories,
        # select directories of files, and even save files edited by the application.
        # In this example, I will use 4 ways to use this dialog:
        # - Get a directory name
        # - Getting a single file name
        # - Getting multiple file names
        # - Get a save file name

        dialog3 = QGroupBox(title='QFileDialog')
        dialog3_layout = QHBoxLayout()
        self.dialog3_button = QPushButton('Open Dir')
        self.dialog3_comboBox = QComboBox(editable=False)
        self.dialog3_comboBox.addItems(['Get Dir', 'Get File', 'Get Files',' Get Save File'])
        dialog3_layout.addWidget(self.dialog3_comboBox)
        dialog3_layout.addWidget(self.dialog3_button)
        dialog3.setLayout(dialog3_layout)

        self.dialog3_button.clicked.connect(self.dialog3_button_pressed)

        # Demo 4: QFontDialog

        # This dialog allows for text customization, including the font, style,
        # size, etc., and a preview of the text with selected properties.
        # Note that it recognizes only the installed fonts in the system.

        dialog4 = QGroupBox(title='QFontDialog')
        dialog4_layout = QVBoxLayout()
        self.dialog4_button = QPushButton('Press me for fonts')
        self.dialog4_label = QLabel('Sample text')
        dialog4_layout.addWidget(self.dialog4_button)
        dialog4_layout.addWidget(self.dialog4_label)
        dialog4.setLayout(dialog4_layout)

        self.dialog4_button.clicked.connect(self.dialog4_button_pressed)

        # Demo 5: QColorDialog

        # The QColorDialog is a window that lets the user select a color from
        # a color map or by specifying the hexadecimal code of the desired color.
        # In this example, the selected color from the window will change the
        # label in the group box.

        dialog5 = QGroupBox(title='QColorDialog')
        dialog5_layout = QVBoxLayout()
        self.dialog5_comboBox = QComboBox(editable=False)
        self.dialog5_comboBox.addItems(['Text Color','Background Color'])
        dialog5_button = QPushButton('Push me for colors')
        self.dialog5_label = QLabel('Some Text')
        self.dialog5_label.setAutoFillBackground(True) # Set for automatic color change
        dialog5_layout.addWidget(self.dialog5_comboBox)
        dialog5_layout.addWidget(dialog5_button)
        dialog5_layout.addWidget(self.dialog5_label)
        dialog5.setLayout(dialog5_layout)

        dialog5_button.clicked.connect(self.dialog5_button_pressed)

        # Demo 6: QInputDialog

        # A QInputDialog is a window which allows the user to enter a specific 
        # type of value like text, integer, etc., with an embedded input widget 
        # (i.e. QLineEdit).

        dialog6 = QGroupBox(title='QInputDialog')
        dialog6_layout = QVBoxLayout()
        self.dialog6_comboBox = QComboBox(editable=False)
        self.dialog6_comboBox.addItems(['Text', 'Int', 'Float', 'Item'])
        self.dialog6_button = QPushButton('Press me for an input')
        self.dialog6_label = QLabel('Placeholder text')
        dialog6_layout.addWidget(self.dialog6_comboBox)
        dialog6_layout.addWidget(self.dialog6_button)
        dialog6_layout.addWidget(self.dialog6_label)
        dialog6.setLayout(dialog6_layout)

        self.dialog6_button.clicked.connect(self.dialog6_button_pressed)

        mainLayout.addWidget(dialog1)
        mainLayout.addWidget(dialog2)
        mainLayout.addWidget(dialog3)
        mainLayout.addWidget(dialog4)
        mainLayout.addWidget(dialog5)
        mainLayout.addWidget(dialog6)
        self.setLayout(mainLayout)

    def dialog1_button_pressed(self):
        state = self.Dialog1.exec()
        if state == QDialog.DialogCode.Accepted:
            self.dialog1_positionLabel.setText(f'Position: {self.Dialog1.position}')
            self.dialog1_osLabel.setText(f'Favorite OS: {self.Dialog1.os}')

    def dialog2_button_pressed(self):
        state = self.Dialog2.exec()
        if state == QDialog.DialogCode.Accepted:
            self.dialog2_label.setText(f'Your position is {self.Dialog2.position} and your favorite OS is {self.Dialog2.os}')

    def dialog3_button_pressed(self):
        selected = self.dialog3_comboBox.currentText()
        fileOptions = QFileDialog.Option
        if selected == 'Get Dir':
            dir = QFileDialog.getExistingDirectory(self,
                                                   'Open Directory',
                                                   './',
                                                   fileOptions.ShowDirsOnly | fileOptions.DontResolveSymlinks )
            print(f'The selected directory is {dir}')

        elif selected == 'Get File':
            filename,_ = QFileDialog.getOpenFileName(self,
                                                     'Open File',
                                                     './',
                                                     'Images (*.png, *.xpm, *.jpg);;All files(*.*)')
            print(f'The chosen file is {filename}')
        elif selected == 'Get Files':
            filenames,_ = QFileDialog.getOpenFileNames(self,
                                                       'Open Files',
                                                       './',
                                                       'Images (*.png, *.xpm, *.jpg);;All files(*.*)')
            print('The selected files are:')
            for f in filenames:
                print(f)
        else: # This does not save a file, it just gets the name and path
            filename,_ = QFileDialog.getSaveFileName(self,
                                                     'Save File',
                                                     './',
                                                     'Images (*.png, *.xpm, *.jpg);;All files(*.*)')
            print(f'The file to save is {filename}')

    def dialog4_button_pressed(self):
        # This specific QFontDialog method call does not require an initial
        # QFont object, but one can be specified as a default.
        ok, font = QFontDialog.getFont(self)
        if ok:
            self.dialog4_label.setFont(font)

    def dialog5_button_pressed(self):
        option = self.dialog5_comboBox.currentText()
        palette = self.dialog5_label.palette() # Gets the label current visual config
        
        if option == 'Text Color':
            color = palette.color(QPalette.ColorRole.WindowText) # Base color
            chosenColor = QColorDialog.getColor(color, self,
                                                'Choose text color')
            
            # The used setColor method only uses the ColorRole and color as inputs
            palette.setColor(QPalette.ColorRole.WindowText, chosenColor)
            self.dialog5_label.setPalette(palette)
        else:
            color = palette.color(QPalette.ColorRole.Window) # Base color
            chosenColor = QColorDialog.getColor(color, self,
                                                'Choose background color')
            palette.setColor(QPalette.ColorRole.Window, chosenColor)
            self.dialog5_label.setPalette(palette)

    def dialog6_button_pressed(self):
        inputType = self.dialog6_comboBox.currentText()
        
        if inputType == 'Text':
            text, ok = QInputDialog.getText(self, 'getText','Enter your name:')
            if ok:
                self.dialog6_label.setText(text)
        elif inputType == 'Int':
            value, ok = QInputDialog.getInt(self, 'getInt','Select a value between 100 and 200:',
                                            150,100,200)
            if ok:
                self.dialog6_label.setText(f'{value}')
        elif inputType == 'Float':
            # By default, it only allows a single decimal digit
            value, ok = QInputDialog.getDouble(self, 'getDouble','Select a value between 100 and 200:',
                                              150,100,200)
            if ok:
                self.dialog6_label.setText(f'{value}')
        else:
            item, ok = QInputDialog.getItem(self, 'getItem', 'Select a season',
                                            ['Spring', 'Summer', 'Fall', 'Winter'],
                                            editable=False)
            if ok:
                self.dialog6_label.setText(item)


class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.position = ''
        self.os = ''

        vLayout = QVBoxLayout()

        hLayout1 = QHBoxLayout()
        positionLabel = QLabel('Position: ')
        self.positionEdit = QLineEdit()
        hLayout1.addWidget(positionLabel)
        hLayout1.addWidget(self.positionEdit)
        vLayout.addLayout(hLayout1)

        hLayout2 = QHBoxLayout()
        osLabel = QLabel('Favorite OS: ')
        self.osEdit = QLineEdit()
        hLayout2.addWidget(osLabel)
        hLayout2.addWidget(self.osEdit)
        vLayout.addLayout(hLayout2)

        hLayout3 = QHBoxLayout()
        spacer = QSpacerItem(40,20, QSP.Policy.Expanding, QSP.Policy.Fixed)
        okButton = QPushButton('Ok')
        okButton.clicked.connect(self.ok)
        cancelButton = QPushButton('Cancel')
        cancelButton.clicked.connect(self.cancel)
        hLayout3.addItem(spacer)
        hLayout3.addWidget(okButton)
        hLayout3.addWidget(cancelButton)
        vLayout.addLayout(hLayout3)

        self.setLayout(vLayout)
        
    def ok(self):
        self.position = self.positionEdit.text()
        self.os = self.osEdit.text()
        self.setResult(QDialog.DialogCode.Accepted)
        self.accept()
    
    def cancel(self):
        self.setResult(QDialog.DialogCode.Rejected)
        self.reject()

class ButtonsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.position = ''
        self.os = ''

        mainLayout = QVBoxLayout()

        hLayout1 = QHBoxLayout()
        positionLabel = QLabel('Position: ')
        self.positionEdit = QLineEdit()
        hLayout1.addWidget(positionLabel)
        hLayout1.addWidget(self.positionEdit)
        mainLayout.addLayout(hLayout1)

        hLayout2 = QHBoxLayout()
        osLabel = QLabel('Favorite OS: ')
        self.osComboBox = QComboBox(editable=False)
        self.osComboBox.addItems(['Windows','Linux','MacOS'])
        hLayout2.addWidget(osLabel)
        hLayout2.addWidget(self.osComboBox)
        mainLayout.addLayout(hLayout2)

        self.stdButton = QDialogButtonBox.StandardButton

        self.buttonBox = QDialogButtonBox(self.stdButton.Cancel|self.stdButton.Ok
                                     |self.stdButton.Open|self.stdButton.Save
                                     |self.stdButton.Yes)
        self.buttonBox.clicked.connect(self.button_box_clicked)

        mainLayout.addWidget(self.buttonBox)

        self.setLayout(mainLayout)

    def button_box_clicked(self, button):
        buttonType = self.buttonBox.standardButton(button)

        if buttonType == self.stdButton.Ok:
            self.position = self.positionEdit.text()
            self.os = self.osComboBox.currentText()
            self.accept()
        elif buttonType == self.stdButton.Cancel:
            self.reject()
        elif buttonType == self.stdButton.Save:
            print('Save')
        elif buttonType == self.stdButton.SaveAll:
            print('Save All')
        elif buttonType == self.stdButton.Open:
            print('Open')
        else:
            print('Some other button')
