import sys
from PyQt5.Qt import *


class MainWnd(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('title')
        self.resize(600, 400)
        self.set_label()
        self.set_button()

    def set_label(self):
        pass

    def set_button(self):
        pass


# 1、创建实例
app = QApplication(sys.argv)
# 2、窗体、控件主要类型
mainWnd = MainWnd()
mainWnd.show()
# 3、消息循环,只有通过窗体点击才能结束程序
sys.exit(app.exec_())

