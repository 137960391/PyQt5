import sys
from PyQt5.Qt import *


class MainWnd(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('title')
        self.resize(600, 400)
        self.init()

    def init(self):

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = MainWnd()
    mainWnd.show()
    sys.exit(app.exec_())
