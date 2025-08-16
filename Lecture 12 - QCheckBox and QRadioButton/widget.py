from PySide6.QtWidgets import QWidget, QGroupBox, QRadioButton, QCheckBox, QHBoxLayout, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QCheckBox and QRadioButton')

        # Checkbox for operating system
        os = QGroupBox('Choose operating system')

        # For each item to be added in the groupbox, a checkbox has to be created
        windows = QCheckBox('Windows')
        linux = QCheckBox('Linux')
        mac = QCheckBox('Mac')

        # Slot configuration
        # windows.toggled.connect(self.windows_box_toggled)
        # linux.toggled.connect(self.linux_box_toggled)
        # mac.toggled.connect(self.mac_box_toggled)

        # To add checkboxes to the group box widget, an intermidiate
        # layout has to be populated, and then set up inside the widget
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        layout = QVBoxLayout()
        layout.addWidget(os)

        self.setLayout(layout)
