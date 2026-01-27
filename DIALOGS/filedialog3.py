from PyQt6.QtWidgets import *
import os

app = QApplication([])
root = QWidget()

root.setWindowTitle("Reading Folder file using File Dialog")

root.setFixedSize(620,410)

def showcontent():
    result = QFileDialog.getExistingDirectory(root,"Open Folder","c:")
    
    if result!="":
        line.setText(result)
        filelist = os.listdir(result)
        for f in filelist:
            textbox.append(result+"/"+f)

line = QLineEdit(root)

button = QPushButton("Browse")
button.setStyleSheet("background-color:red;color:white")

label = QLabel("Folder Contents: ")
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