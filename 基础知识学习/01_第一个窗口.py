# 导入sys模块
import sys
# 导入PyQt5的QtWidgets和QtCore模块
from PyQt5 import QtWidgets

# 创建一个QApplication实例，用于管理应用程序的事件循环和GUI基础设施
app = QtWidgets.QApplication(sys.argv)
# 创建一个QWidget实例，作为所有用户界面对象的基类
widget = QtWidgets.QWidget()
# 设置QWidget窗口的大小为720x360像素
widget.resize(720, 360)
# 设置QWidget窗口的标题为'hello'
widget.setWindowTitle('hello')
# 显示QWidget窗口
widget.show()
# 启动应用程序的事件循环，直到应用程序被终止或退出
sys.exit(app.exec_())


