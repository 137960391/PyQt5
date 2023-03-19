import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
# from excel import deal_excel_data
from excel import DataInfo
import threading
from configparser import ConfigParser


class DragDropWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.resize(540, 30)
        self.label.setStyleSheet('border: 1px solid black')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            self.label.setText(files[0])

            # 提取文件名中的日期，并显示在textbox1中
            date_str = self.extract_date(files[0])
            if date_str:
                self.parent().textbox1.setText(date_str)

    def extract_date(self, content):
        # 在 content 中提取日期的逻辑，这里用一个简单的正则表达式实现
        import re
        pattern = r'\d{4}-\d{2}-\d{2}'
        match = re.search(pattern, content)
        if match:
            return match.group()
        else:
            return None


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drag and Drop')
        self.resize(600, 400)
        self.initUI()

    def initUI(self):
        style_sheet = """
                    QWidget {
                        background-color: #F5F5F5;
                        font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
                        font-size: 14px;
                        color: #333;
                    }

                    QLabel {
                        font-size: 16px;
                        font-weight: bold;
                    }

                    QLineEdit, QPushButton {
                        border-radius: 5px;
                        border: 1px solid #ddd;
                        padding: 8px;
                        min-height: 30px;
                    }

                    QPushButton {
                        background-color: #4CAF50;
                        color: #fff;
                        font-size: 16px;
                        font-weight: bold;
                        border: none;
                        margin-top: 20px;
                    }

                    QPushButton:hover {
                        background-color: #3E8E41;
                        cursor: pointer;
                    }

                    QGridLayout {
                        margin: 0;
                        padding: 0;
                    }

                    QHBoxLayout {
                        margin: 0;
                        padding: 0;
                    }

                    QVBoxLayout {
                        margin: 20px;
                        padding: 0;
                    }

                    DragDropWidget {
                        border: 1px solid black;
                        background-color: #fff;
                        min-height: 50px;
                        margin-top: 10px;
                        margin-bottom: 20px;
                    }

                    DragDropWidget QLabel {
                        font-size: 16px;
                        margin: 10px;
                    }
                """
        self.setStyleSheet(style_sheet)
        layout = QVBoxLayout(self)

        # 添加一个水平布局，用于左右排版日期和销售目标的标签和文本框
        top_row_layout = QHBoxLayout()
        layout.addLayout(top_row_layout)

        # 添加日期标签和文本框
        top_row_layout.addWidget(QLabel('日期：'))
        self.textbox1 = QLineEdit(self)
        top_row_layout.addWidget(self.textbox1)
        self.textbox1.textChanged.connect(self.on_textbox1_text_changed)


        # 添加销售目标标签和文本框
        top_row_layout.addWidget(QLabel('当月销售目标：'))
        self.textbox2 = QLineEdit(self)
        top_row_layout.addWidget(self.textbox2)

        # 添加文件拖拽区的标签和 DragDropWidget 控件
        layout.addWidget(QLabel('当日文件拖拽区:'))
        self.dd1 = DragDropWidget(self)
        self.dd1.label.resize(560,50)
        layout.addWidget(self.dd1)

        layout.addWidget(QLabel('主数据拖拽区:'))
        self.dd2 = DragDropWidget(self)
        layout.addWidget(self.dd2)
        self.dd2.label.resize(560, 50)
        # 添加按钮并连接生成表单的函数
        self.button = QPushButton('生成表单')
        self.button.clicked.connect(self.printpaths)
        layout.addWidget(self.button)

    def printpaths(self):
        if self.get_excel_type(self.dd2.label.text()) == '.xls':
            QMessageBox.warning(self, "Warning", "主数据拖拽区文件格式错误，请转换为.xlsx")
            return
        if self.get_excel_type(self.dd1.label.text()) == '.xlsx':
            QMessageBox.warning(self, "Warning", "当日文件拖拽区文件格式错误，请转换为.xls")
            return
        my_thread = threading.Thread(target=self.start_excel, args=(self.dd1.label.text(),
                                self.dd2.label.text(), self.textbox1.text(), self.textbox2.text()))
        if self.dd1.label.text() == '' or self.dd2.label.text() == '':
            QMessageBox.warning(self, "Warning", "未拖入文件")
            return
        if self.textbox2.text() == '':
            QMessageBox.warning(self, "Warning", '请在配置项中添加当月销售目标或手动输入')
            return
        if self.dd1.label.text() != '' and self.dd2.label.text() != '' and self.dd1.label.text() != '':
            # 禁用按钮
            self.button.setEnabled(False)
            # 启动多线程
            my_thread.start()
            # 在多线程结束后恢复按钮文本和状态
            self.button.setText('表单生成中')
            alive_thread = threading.Thread(target=self.is_alive, args=(my_thread,))
            alive_thread.start()
            # self.button.setText('表单生成中')



    @staticmethod
    def start_excel(arg1, arg2, arg3, arg4):
        DataInfo(arg1, arg2, arg3, arg4)
        pass

    def is_alive(self, th):
        th.join()
        # 恢复按钮
        self.button.setText('生成表单')
        self.button.setEnabled(True)

    def extract_date(self, content):
        date_str = None
        # 在 content 中提取日期的逻辑
        return date_str

    def on_textbox1_text_changed(self, event):
        text = self.textbox1.text()
        month = int(text.split('-')[1])  # Get the month from the date string
        # Read the config file
        config = ConfigParser()
        config.read('../../config.ini')
        # Get the value for the corresponding month
        section_name = 'sale_money'
        option_name = f'{month}月'
        value = config.get(section_name, option_name)
        self.textbox2.setText(value)
        pass

    @staticmethod
    def get_excel_type(filename):

        if filename.endswith('.xlsx'):
            return '.xlsx'
        elif filename.endswith('.xls'):
            return '.xls'
        else:
            return -1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
