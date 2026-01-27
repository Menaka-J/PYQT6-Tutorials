from PyQt6.QtWidgets import *

app = QApplication([])
root = QWidget()

root.setWindowTitle("ReadinWritingg text file using File Dialog")

root.setFixedSize(620,410)

def savecontent():
    result = QFileDialog.getSaveFileName()
    text = textbox.toPlainText()
    
    if result[0]!="":
        file = open(result[0],"w")
        file.write(text) 
        file.close()

label = QLabel("Saving File using QFileDialog ")
label.setStyleSheet("color:blue;padding:15px")

textbox = QTextEdit(root)
textbox.setStyleSheet("background-color:purple;color:white;padding:15px")

button = QPushButton("Save file")
button.setStyleSheet("background-color:red;color:white")

button.clicked.connect(savecontent)

# layout 
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(textbox)
layout.addWidget(button)

root.setLayout(layout)
root.show()
app.exec()