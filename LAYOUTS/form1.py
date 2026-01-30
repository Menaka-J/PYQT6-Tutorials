from PyQt6.QtWidgets import *

app=QApplication([])
root = QWidget()

root.setWindowTitle("Form layout using adding widget")
root.setGeometry(400,400,500,500)

label1 = QLabel("Name: ")
label2 = QLabel("Age: ")
label3 = QLabel("Department: ")

input1 = QLineEdit()
input2 = QLineEdit()
input3 = QLineEdit()

button = QPushButton("Submit")
button.setStyleSheet("color:white;background-color:green")

#layout
layout = QFormLayout()

layout.addWidget(label1)
layout.addWidget(input1)
layout.addWidget(label2)
layout.addWidget(input2)
layout.addWidget(label3)
layout.addWidget(input3)
layout.addWidget(button)

root.setLayout(layout)

root.show()
app.exec()