import sys
from PyQt5 import QtWidgets

# 将 sys.stdout 重定向到一个文件
sys.stdout = open('./help.txt', 'w+')
# 输出到文件中
help(QtWidgets)
# 关闭文件
sys.stdout.close()
# 恢复 sys.stdout 的默认行为
sys.stdout = sys.__stdout__
# 恢复输出到控制台



