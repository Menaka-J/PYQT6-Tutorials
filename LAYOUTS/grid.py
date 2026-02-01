from PyQt6.QtWidgets import *

app=QApplication([])
root=QWidget()

root.setWindowTitle("Grid layout")
# root.setFixedSize(400,400)
root.setGeometry(300,300,300,300)

button1 = QPushButton("Java")
button2 = QPushButton("C++")
button3 = QPushButton("Python")
button4 = QPushButton("C#")

button1.setStyleSheet("background-color:red;color:white")
button2.setStyleSheet("background-color:greeen;color:white")
button3.setStyleSheet("background-color:purple;color:white")
button4.setStyleSheet("background-color:orange;color:white")

#layout
layout = QGridLayout()

layout.addWidget(button1,0,0)
layout.addWidget(button2,0,1)
layout.addWidget(button3,1,0)
layout.addWidget(button4,1,1)

root.setLayout(layout)

root.show()
app.exec()