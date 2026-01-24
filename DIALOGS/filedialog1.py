from PyQt6.QtWidgets import *

app = QApplication([])
root = QWidget()

root.setWindowTitle("Reading text file using File Dialog")

root.setFixedSize(620,410)

def showcontent():
    result = QFileDialog.getOpenFileName(root,"Open Dialog")
    
    if result[0]!="":
        line.setText(result[0])
        file = open(result[0])
        textbox.setText(file.read())

line = QLineEdit(root)

button = QPushButton("Browse")
button.setStyleSheet("background-color:red;color:white")

label = QLabel("File Contents: ")
textbox = QTextEdit(root)
textbox.setStyleSheet("background-color:purple;color:white")

button.clicked.connect(showcontent)

# layout 
layout = QVBoxLayout()
layout.addWidget(line)
layout.addWidget(button)
layout.addWidget(label)
layout.addWidget(textbox)

root.setLayout(layout)
root.show()
app.exec()