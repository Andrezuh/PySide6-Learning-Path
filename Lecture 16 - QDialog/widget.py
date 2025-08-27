from PySide6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QComboBox, 
                               QPushButton, QLabel, QLineEdit, QGroupBox,
                               QDialog, QSpacerItem, QSizePolicy as QSP)

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

        self.Dialog = Dialog()
        dialog1_button.clicked.connect(self.dialog1_button_pressed)

        mainLayout.addWidget(dialog1)
        self.setLayout(mainLayout)

    def dialog1_button_pressed(self):
        state = self.Dialog.exec()
        if state == QDialog.DialogCode.Accepted:
            self.dialog1_positionLabel.setText(f'Position: {self.Dialog.position}')
            self.dialog1_osLabel.setText(f'Favorite OS: {self.Dialog.os}')

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









