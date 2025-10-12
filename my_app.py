# write the code for main app and first screen


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_win import *

class Mainwin(QWidget):
       def__init__(self):
              super().__init__()
              self.initUI()
              self.connects()
              self.set_appear()
              self.show()

       def initUI(self):
              self.btn_next = QpushButton(txt_next, self)
              self.hello_text = QLabel(txt_instruction)

              self.layout_line = QVBoxLayout()
              self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
              self.layout_line.addWidget(self.instuctions, alignment = Qt.AlignLeft)
              self.layout_line.addWidget(self.btn_next, alignment = Qt.ALignCenter)

       def next_click(self):
              self.tw = TestWin()
              self.hide()
       def connects(self):
              self.btn_next.clicked.connect(self.next_click)


       def set_appear([]):
              self.setWindowTitle(txt_title)
              self.resize(win_width, win_heigth)
              self.move(win_x,win_y)


app = QApplication([])
mw = MainWIN()
app.exec_()
              
       
