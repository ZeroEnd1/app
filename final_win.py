from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    
    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.Layout_line = QVBoxLayout()
        self.Layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.Layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.setLayout(self.Layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
