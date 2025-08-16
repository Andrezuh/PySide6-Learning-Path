from PySide6.QtWidgets import QWidget, QGroupBox, QRadioButton, QCheckBox, QHBoxLayout, QVBoxLayout, QButtonGroup

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
        windows.toggled.connect(self.windows_box_toggled)
        linux.toggled.connect(self.linux_box_toggled)
        mac.toggled.connect(self.mac_box_toggled)

        # To add checkboxes to the group box widget, an intermidiate
        # layout has to be populated, and then set up inside the widget
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)


        # Exclusive checkboxed for drinks
        drinks = QGroupBox('Choose your drink')

        beer = QCheckBox('Beer')
        juice = QCheckBox('Juice')
        coffee = QCheckBox('Coffee')
        beer.setChecked(True)

        # To set an exclusive checkbox selection, all the widgets
        # have to be inserted into a grouping
        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        # Radio buttons for answers
        # Similar to checkboxes, radio buttons are round and exclusive in nature
        answers = QGroupBox('Choose Answer')
        answer_a = QRadioButton('A')
        answer_b = QRadioButton('B')
        answer_c = QRadioButton('C')

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    # Setting up slots
    def windows_box_toggled(self, checked):
        if checked:
            print('Windows box checked')
        else:
            print('Windows box unchecked')

    def linux_box_toggled(self, checked):
        if checked:
            print('Linux box checked')
        else:
            print('Linux box unchecked')

    def mac_box_toggled(self, checked):
        if checked:
            print('Mac box checked')
        else:
            print('Mac box unchecked')