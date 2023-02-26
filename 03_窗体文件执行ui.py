import sys                          # 导入sys模块
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtWidgets        # 导入PyQt5.QtWidgets模块
from PyQt5.uic import loadUi       # 导入PyQt5.uic.loadUi模块


def b_click():
    print('按钮被点击!')


# 创建一个Qt应用程序对象
app = QtWidgets.QApplication(sys.argv)
# 创建一个QWidget窗口并打印出来
# print(QtWidgets.QWidget())
# 打印QWidget类
# print(QtWidgets.QWidget)
# 从UI文件中加载UI并将其实例化为一个QWidget对象，使用类型提示指定对象类型
wnd: QtWidgets.QWidget = loadUi('03_ui.ui')
# 获取ui中的btn对象
btn = wnd.findChild(QtWidgets.QPushButton, 'pushButton')
# 连接btn对象信号槽
btn.clicked.connect(b_click)
# 显示QWidget对象
wnd.show()
# 运行应用程序的事件循环并退出程序
sys.exit(app.exec_())

