from PySide6.QtWidgets import QWidget, QSizePolicy, QPushButton, QGridLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QGridLayout Demo')

        button_1 = QPushButton('One')
        button_2 = QPushButton('Two')
        button_3 = QPushButton('Three')
        button_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Allows for button to occupy all allocated space
        button_4 = QPushButton('Four')
        button_5 = QPushButton('Five')
        button_6 = QPushButton('Six')
        button_7 = QPushButton('Seven')

        # In grid layout, you specify where the widget goes in rows and columns. e.g: (0,0), (1,2), (2,2)
        # If the widget takes up more space, the amount of rows/columns it uses must also be specified
        # Example 1: Widget in row 1, column 2 
        # -> QGridLayout().addWidget(QWidget, 1,2)
        # Example 2: The same widget in the same position, but using 3 rows below and 2 columns to the right
        # -> QGridLayout().addWidget(QWidget, 1,2, 3,2)

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1, 0,0)
        grid_layout.addWidget(button_2, 0,1, 1,2)
        grid_layout.addWidget(button_3, 1,0, 2,1)
        grid_layout.addWidget(button_4, 1,1)
        grid_layout.addWidget(button_5, 1,2)
        grid_layout.addWidget(button_6, 2,1)
        grid_layout.addWidget(button_7, 2,2)

        self.setLayout(grid_layout)