from PyQt6.QtWidgets import *

app = QApplication([])
root = QWidget()

root.setWindowTitle("Horizontal box layout")
root.setFixedSize(500,500)

bt1 = QPushButton("java")
bt2 = QPushButton("C++")
bt3 = QPushButton("Python")

bt1.setStyleSheet("background-color:red;color:white")
bt2.setStyleSheet("background-color:green;color:white")
bt3.setStyleSheet("background-color:yellow;color:white")

#QHBoxLayout
layout = QHBoxLayout()

layout.addWidget(bt1)
layout.addWidget(bt2)
layout.addWidget(bt3)

root.setLayout(layout)

root.show()
app.exec()
