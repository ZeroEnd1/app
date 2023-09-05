from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from instr import *
from second_win import *

class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_txt= QLabel(txt_hello)
        self.instrustion = QLabel(txt_instruction)

        self.Layout_line = QVBoxLayout()
        self.Layout_line.addWidget(self.hello_txt, alignment=Qt.AlignLeft)
        self.Layout_line.addWidget(self.instrustion, alignment=Qt.AlignLeft)
        self.Layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.Layout_line)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = Mainwin()
app.exec_()
