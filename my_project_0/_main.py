# encoding = utf-8
# Version: 0.01
# public_mod
import os
import sys
import json
import hashlib
import threading

from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from playsound import playsound  # 用于播放声音的模块


class SI:
    """公共访问对象"""
    welcome_window = None  #欢迎窗口
    user_login_window = None  #登录
    user_account_setup = None  #用户账户设置
    administrator = None  #管理员
    production = None  #生产
    warehouse = None  #仓库
    clerk = None  #文员
    business = None  #业务
    activation_window = None  #激活此软件
    activation = None  #序列号激活码模块
    the_hash = None  #加密模块
    successful = None  #激活成功
    key_path = None  #激活码路径



class Asymmetric:
    """非对称加密模块的类"""
    
    @staticmethod
    def encryption(answer):
        """sha512加密,序列号"""
        key = 'encryption_2021' * 1024  #加盐
        answer = answer + key
        serial_number = hashlib.sha512(answer.encode('utf-8')).hexdigest()
        return serial_number

    @staticmethod
    def finally_encryption(answer):
        """sha512加密,序列号和文件加密"""
        key = 'encryption_1024.HELLO_WORD' * 1024  #加盐
        answer = answer + key
        finally_password = hashlib.sha512(answer.encode('utf-8')).hexdigest()
        return finally_password


class Run_Thread:
    """多线程模块创建"""
    def __init__(self, aims):
        """多线程"""
        self.aims = threading.Thread(target=aims, daemon=True)  # 设置为主线程守护模式
        self.aims.start()  # 启动

class File_Path:
    """这里获取所需写入数据的路径并写入值"""
    @staticmethod
    def is_path_exist():
        """判断所需路径是否存在"""

        key_path_1 = os.path.join(base_path, 'key')
        key_path_2 = os.path.join(base_path, 'key\\key.json')
        result_1 = os.path.exists(key_path_1)
        result_2 = os.path.exists(key_path_2)
        if result_1 == True and result_2 == True:
            pass
        elif result_1 == True and result_2 == False:
            with open(key_path_2, 'w') as f:
                f.write('\"\"')
        else:
            os.mkdir('key')
            with open(key_path_2, 'w') as f:
                f.write('\"\"')
                
    @staticmethod
    def value_path(activation_value):
        """将key的值写入json文件"""
        key_path = r'key\key.json'
        with open(key_path, 'w') as f:
            json.dump(activation_value, f)

    @staticmethod
    def judge_activation_code():
        """获取key.json里的激活码数据"""
        key_path = r'key\key.json'
        with open(key_path, 'r') as f:
            answer = json.load(f)
        return answer

class Activation:
    """用于生成验证码的值"""
    def get_value(self):
        """使用固定路径进行验证码的生成"""
        self.aim_path = os.path.expanduser('~')  #用户路径
        return self.aim_path

    
class Hash:
    """用于得到序列号和激活码"""
    
    @staticmethod
    def hash_value():
        """得到加密的sha512码,序列号"""
        act_get_value = Activation()  #实例化生成验证码的类
        user_path = act_get_value.get_value()  #得到用户账户作为加密明文
        encrypt = Asymmetric()  #实例化非对称加密模块(sha512)
        serial_number = encrypt.encryption(user_path)  #得到加密后的密文(序列号)
        return serial_number
    
    @staticmethod
    def finally_value():
        """得到激活码的唯一值"""
        serial_number = Hash.hash_value()
        encrypt = Asymmetric()
        finally_value = encrypt.finally_encryption(serial_number)
        return finally_value

class Activation_Window:
    """激活界面"""
    def __init__(self):
        """初始化激活界面"""
        self.window = QUiLoader().load('activation_window.ui')
        SI.the_hash = Hash()  # 实例化序列号和激活码的类
        result = SI.the_hash.hash_value()  # 生成序列号
        self.window.lineEdit_2.setText(result)  # 显示序列号给用户
        self.window.lineEdit.setPlaceholderText('请在这里输入您的激活码！')
        self.window.pushButton.clicked.connect(self.to_activation_code)

    def to_activation_code(self):
        """获取用户输入的激活码,进行判断并做出响应"""
        activation_text = self.window.lineEdit.text()  # 获取用户输入
        self.window.lineEdit.clear() # 清空文本
        answer = SI.the_hash.finally_value()  # 获取正确的激活码
        if activation_text == answer: # 激活成功 显示激活成功的页面并写进key中
            SI.key_path.value_path(answer)
            self.window.close() # 关闭自身,打开主窗体循环
            SI.successful = Successful_Window()  # 实例化成功界面对象存入SI中
            SI.successful.window.show()
        else: # 不满足则程序报错退出
            QMessageBox.information(self.window, '激活失败', '激活码验证失败\n即将退出')
            self.window.close()

            
class Successful_Window:
    """激活成功后显示的页面类"""
    def __init__(self):
        self.window = QUiLoader().load('successful_window.ui')
        self.window.pushButton.clicked.connect(self.to_go_next)
        
    def to_go_next(self):
        """"关闭自身，并继续往下执行"""
        self.window.close()
        SI.welcome_window = Welcom_Window()  # 实例化对象到ShareInfo
        SI.welcome_window.window.show()
    
class Welcom_Window:
    """欢迎界面的类,内置各种功能"""
    
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        Run_Thread(self.sounds)  # 播放声音
        self.window = QUiLoader().load('main_window.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.pushButton.clicked.connect(self.user_login)  #账户登录
        self.window.pushButton_2.clicked.connect(self.account_setup)  #密码设置

    def user_login(self):
        """登录的处理函数"""
        self.window.hide()  #隐藏主窗口
        SI.user_login_window = User_Login()  #实例化用户登录界面，并将其存入SI模块
        SI.user_login_window.window.show()  #展示用户界面

    def account_setup(self):
        """账户密码设置的处理函数"""
        self.window.hide()  #隐藏
        SI.user_account_setup = Account_Setup()  #实例化密码设置界面，并将其存入SI模块
        SI.user_account_setup.window.show()

    def sounds(self):
        """用于播放声音"""
        playsound('music\\_000.mp3')

    
class User_Login:
    """用户登录后的界面类"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        self.window = QUiLoader().load('login_window.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.action_1.triggered.connect(self.sign_out)

    def sign_out(self):
        """用于返回主界面"""
        self.window.close()  #关闭此登录窗口
        SI.welcome_window.window.show()  #再次展示此窗口
        
        
class Account_Setup(User_Login):
    """账户设置界面,继承了User_Login"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        super().__init__()
        self.window = QUiLoader().load('account_window.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.action_1.triggered.connect(self.sign_out)  #返回主菜单
        self.window.pushButton.clicked.connect(self.business_option)  #业务密码设置
        self.window.pushButton_2.clicked.connect(self.clerk_option)  #文员密码设置
        self.window.pushButton_3.clicked.connect(self.warehouse_option)  #仓库密码设置
        self.window.pushButton_4.clicked.connect(self.production_option)  #生产密码设置
        self.window.pushButton_5.clicked.connect(self.administrator_option)  #管理员密码设置
        
    def administrator_option(self):
        """管理员账户密码设置的处理函数"""
        self.window.hide()  #隐藏窗口
        SI.administrator = Administrator_Option()
        SI.administrator.window.show()  #回显窗口
    
    def production_option(self):
        """生产密码设置"""
        self.window.hide()
        SI.production = Production_Option()
        SI.production.window.show()
    
    def warehouse_option(self):
        """仓库密码设置"""
        self.window.hide()
        SI.warehouse = Warehouse_Option()
        SI.warehouse.window.show()
    
    def clerk_option(self):
        """文员密码设置"""
        self.window.hide()
        SI.clerk = Clerk_Option()
        SI.clerk.window.show()
    
    def business_option(self):
        """业务密码设置"""
        self.window.hide()
        SI.business = Business_Option()
        SI.business.window.show()

class Administrator_Option(User_Login):
    """管理员界面设置，此后的所有相似界面都继承于此"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        super().__init__()
        self.window = QUiLoader().load('administrator_option.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.action_1.triggered.connect(self.sign_out)
        
    def sign_out(self):
        """用于返回主界面"""
        self.window.close()  #关闭此登录窗口
        SI.user_account_setup.window.show()  #再次展示此窗口        
    
class Production_Option(Administrator_Option):
    """生产密码设置界面"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        super().__init__()
        self.window = QUiLoader().load('production_option.ui')  
        self.window.action_1.triggered.connect(self.sign_out)
    
class Warehouse_Option(Administrator_Option):
    """仓库密码设置"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        super().__init__()
        self.window = QUiLoader().load('warehouse_option.ui')  
        self.window.action_1.triggered.connect(self.sign_out)
    
class Clerk_Option(Administrator_Option):
    """文员密码设置"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        super().__init__()
        self.window = QUiLoader().load('clerk_option.ui')  
        self.window.action_1.triggered.connect(self.sign_out)
    
class Business_Option(Administrator_Option):
    """业务密码设置"""
    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        super().__init__()
        self.window = QUiLoader().load('business_option.ui')  
        self.window.action_1.triggered.connect(self.sign_out)

class Boot:
    """启动"""
    @staticmethod
    def main():
        """启动主窗口"""
        SI.key_path = File_Path()  #实例化路径的类，并存入SI中
        SI.key_path.is_path_exist() #直接判断是否路径正确,若不正确则创建
        SI.the_hash = Hash()  #实例化生成激活码的列，并存入SI中
        answer_1 = SI.key_path.judge_activation_code()  #json文件中的激活码数值
        answer_2 = SI.the_hash.finally_value()
        if answer_1 == answer_2:  #具有正确的激活码,才能进入此入口
            app = QApplication([])
            SI.welcome_window = Welcom_Window()  #实例化主窗口界面窗口
            SI.welcome_window.window.show()  #展示
            app.exec_()
        else:  #这是注册界面
            app = QApplication([])
            SI.activation_window = Activation_Window()  #实例化激活界面窗口
            SI.activation_window.window.show()
            app.exec_()
            
    
if __name__ == '__main__':
    if getattr(sys, "frozen", False):
        # 在exe中时运行
        base_path = os.path.dirname(sys.executable)
    else:
        # 在python环境中时运行
        base_path = os.path.dirname(os.path.abspath(__file__))
    Boot.main()


