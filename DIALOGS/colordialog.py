from PyQt6.QtWidgets import *

app = QApplication([])
root = QWidget()

root.setWindowTitle("Setting color using Color Dialog")

root.setFixedSize(620,410)

def showcontent():
   res = QColorDialog.getColor()

   if res.isValid():
       textbox.setStyleSheet("background-color:"+res.name())
       
label = QLabel("Color Example ")

textbox = QTextEdit(root)
textbox.setStyleSheet("background-color:purple;color:white")

button = QPushButton("Change Color")
button.setStyleSheet("background-color:green;color:white")

button.clicked.connect(showcontent)

# layout 
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(textbox)
layout.addWidget(button)

root.setLayout(layout)
root.show()
app.exec()