from PyQt5.QtWidgets import QApplication, QWidget, Qlabel, QVBoxtayout, QPushButton

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear (self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt_name = Qlabel(txt_txt_name)
        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_age = Qlabel(txt_age)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)

        self.txt_test1 = Qlabel(txt_test1)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2) 

        self.txt_test2 = Qlabel(txt_test2)       
        self.txt_starttest2 = QPushButton(txt_starttest2) 

        self.txt_test3 = Qlabel(txt_test3)       
        self.txt_starttest3 = QPushButton(txt_starttest3) 
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)        
        self.txt_hinttest3 = QLineEdit(txt_hinttest3) 

        self.txt_timer = Qlabel(txt_timer) 
        self.txt_finalwin = QPushButton(txt_finalwin)       

        self.setLayout (self.layout_line)        
        self.layout_line = QHBoxtayout()
        self.layout_line.addWidget(self.txt_timer, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.txt_finalwin, alignment=Qt.AlignCenter)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

if __name__ == "__main__":
    app = QApplication([])
    

    window1 = TestWin()
    window2 = TestWin()
    
    app.exec_()