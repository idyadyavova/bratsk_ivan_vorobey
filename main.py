import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.pushButton.clicked.connect(self.run_1)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()
        self.do_paint = False

    def run_1(self):
        self.do_paint = True
        self.update()

    def run(self, qp):
        try:
            qp.setPen(QPen(Qt.yellow, 8, Qt.DashLine))
            a = random.randint(40, 400)
            qp.drawEllipse(20, 20, a, a)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
