# encoding = utf-8

# public_mod
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

# private_mod
from _public import SI
from _user_login import *


class Login_Window:
    """欢迎界面的类,内置各种功能"""
    
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        self.window = QUiLoader().load('_login.ui')
        self.window.lineEdit.returnPressed.connect(\
            self.judge_user_login)  #绑定回车按键

    def judge_user_login(self):
        """用户登录判断"""
        text = self.window.lineEdit.text()  #获取用户输入的文本
        SI.info_handle = Info_Handle()
        result = SI.info_handle.info_read()  #得到存储的用户数据
        for key in result:
            if text == result[key]:  #如此效率会更高
                self.window.close()
                SI.main_window = Main_Window()
                SI.main_window.window.show()
                #这里需要根据不同的账户进入不同的界面
                break
        else:
            QMessageBox.information(self.window, \
                                        '登录失败', '口令无效,请输入已授权的口令')


class Main_Window:
    """定义主窗口"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        self.window = QUiLoader().load('_main.ui')
