# Button demo
"""
from PySide6.QtWidgets import QApplication, QPushButton

# The slot: a method which recieves a signal and does something
def button_clicked(state):
    print("You clicked the button, didn't you!", state)

app = QApplication()
button = QPushButton("Press Me")

# The following method can make the button checkable
button.setCheckable(True)

# The signal: emitted from the widget to a slot, in order to
# make an action happen
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

# Slider demo

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

# The slot
def respond_to_slider(data):
    print(f"Slider moved to: {data}")

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(50)

# The signal: The slider detects the current number
# when it's changed, and sends it to the slot method
slider.valueChanged.connect(respond_to_slider)
slider.show()

app.exec()