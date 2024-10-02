# encoding = utf-8

# version_number = 0.03
# public mod
# private mod

from _window import *
from _public import SI


class Boot_Login_Window:
    """启动登录窗口"""
    @staticmethod
    def boot():
        """启动"""
        app = QApplication([])  #实例化窗口
        SI.login_window = Login_Window()  #实例化主窗口界面窗口
        SI.login_window.window.show()  #展示
        app.exec_()  #窗体循环

        
if __name__ == '__main__':
    Boot_Login_Window.boot()
    
