from PyQt6.QtWidgets import *

app = QApplication([])
root = QWidget()

root.setWindowTitle("Setting Font using Font Dialog")

root.setFixedSize(620,410)

def showcontent():
   res = QFontDialog.getFont(root)

   if res[1]==True:
       textbox.setFont(res[0])

label = QLabel("Font Example ")

textbox = QTextEdit(root)
textbox.setStyleSheet("background-color:purple;color:white")

button = QPushButton("Change Font")
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