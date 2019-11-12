from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
import sys
from random import randint as ch
from qq import Ui_MainWindow


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag is True:
            x = ch(0, 500)
            y = ch(0, 600)
            l = ch(0, 500)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            painter.drawEllipse(x, y, l, l)
            self.flag = False


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())