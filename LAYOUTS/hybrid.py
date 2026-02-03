from PyQt6.QtWidgets import *

app=QApplication([])
root = QWidget()

root.setWindowTitle("Form layout using adding widget")
root.setGeometry(400,400,500,500)

button1 = QPushButton("Java")
button2 = QPushButton("Python")
button3 = QPushButton("C++")
button4 = QPushButton("C#")

button1.setStyleSheet("color:white;background-color:green")
button2.setStyleSheet("color:white;background-color:red")
button3.setStyleSheet("color:white;background-color:purple")
button4.setStyleSheet("color:white;background-color:orange")

#layout
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()

layout1.addWidget(button1)
layout1.addWidget(button2)

layout2.addWidget(button3)
layout2.addWidget(button4)

layout2.addLayout(layout1)

root.setLayout(layout2)

root.show()
app.exec()