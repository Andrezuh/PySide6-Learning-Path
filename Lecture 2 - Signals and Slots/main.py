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