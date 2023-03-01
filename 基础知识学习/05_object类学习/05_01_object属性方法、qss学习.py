
from PyQt5.Qt import *


class MainWnd(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('object学习')
        self.resize(600, 400)
        self.init()

    def init(self):
        self.study_object(self)
        pass

    @staticmethod   # 如果函数中没有用到self则需要加变量
    def study_object(self):
        # ***************object基础*************#
        # obj = QObject
        # # 查看QObject子类
        # # print(obj.__subclasses__())
        # # 查看父类
        # # print(obj.mro())
        # # object名称设置
        # obj_o = QObject()
        # obj_o.setObjectName('obj')
        # print(obj_o.objectName())
        # # object属性设置
        # obj_o.setProperty('math', 20)
        # obj_o.setProperty('language', 20)
        # print(obj_o.property('math'))
        # print(obj_o.dynamicPropertyNames())
        # ***********************************#

        # ***************object案例*************#
        with open('label.qss', 'r') as file:
            qApp.setStyleSheet(file.read())
        label1 = QLabel(self)
        label1.setObjectName('hel')
        label1.setText('label1')
        label1.move(200, 200)
        
        label2 = QLabel(self)
        # 通过设置objectname达到类似css id选择器效果
        # label2.setObjectName('wol')
        # 通过设置property达到类似css 类型选择器
        label2.setProperty('bor', 'yellow')
        label2.setText('label2')
        label2.move(100, 100)
        # qss使用
        # label.setStyleSheet('font-size:50px;color:blue')
        # 文件读取
        # ***********************************#
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWnd = MainWnd()
    mainWnd.show()
    sys.exit(app.exec_())
