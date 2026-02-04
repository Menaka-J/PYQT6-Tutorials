from PyQt6.QtWidgets import *

app = QApplication([])
root = QWidget()

root.setWindowTitle("Vertical box layout")
root.setFixedSize(400,400)

button1 = QPushButton("Java")
button2 = QPushButton("Python")
button3 = QPushButton("C++")

button1.setStyleSheet("background-color:red;color:white")
button2.setStyleSheet("background-color:green;color:white")
button3.setStyleSheet("background-color:purple;color:white")

#layout
layout = QVBoxLayout()

layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)

root.setLayout(layout)

root.show()
app.exec()