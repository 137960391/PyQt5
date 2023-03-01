from PyQt5.Qt import *


class MainWnd(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('')
        self.resize(600, 400)
        self.init(self)

    @staticmethod
    def init(self):

        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        # setParent 设置对象父对象
        obj5.setParent(obj3)
        obj4.setParent(obj3)
        obj3.setParent(obj1)
        obj2.setParent(obj1)

        print('obj1:', obj1)
        print('obj2:', obj2)
        print('obj3:', obj3)
        print('obj4:', obj4)
        print('obj5:', obj5)
        obj5.setObjectName('hello')
        # parent 获取父对象
        # print(obj5.parent())
        # children获取直接值对象，不包括孙子

        # findChild获取某一个子对象,找到一个就结束
        # @para1：查找对象
        # @para2：名称，可以省略
        # @para3：默认递归，Qt.FindDirectChildrenOnly表示只查找儿子
        print('child', obj1.findChild(QObject))
        # findChild获取多个子对象
        # @para1：查找对象
        # @para2：名称，可以省略
        # @para3：默认递归，Qt.FindDirectChildrenOnly表示只查找儿子
        print('children', obj1.findChildren(QObject, '', Qt.FindDirectChildrenOnly))
        # 查找objectName为hello的对象
        print('children', obj1.findChildren(QObject, 'hello'))
        # ***************对象销毁机制*************#
        # 父对象被销毁，子对象跟着被销毁
        obj4.destroyed.connect(lambda: print('obj4销毁'))
        obj5.destroyed.connect(lambda: print('obj5销毁'))
        del obj3
        # ***********************************#
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # mainWnd = MainWnd()
    # mainWnd.show()
    # ***************窗口继承机制*************#
    # 未设置父对象直接展示
    win1 = QWidget()
    win1.setStyleSheet('background-color:red')
    win1.resize(500, 500)
    win1.show()
    win2 = QWidget()
    win2.setStyleSheet('background-color:yellow')
    # 设置父对象后直接依附在父对象上
    win2.setParent(win1)
    win2.resize(500, 300)
    win2.show()
    # ***********************************#

    sys.exit(app.exec_())
