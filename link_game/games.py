# -*- coding: utf-8 -*-
# Powered by "改个什么名字好呢?"
"""
目前程序的一些问题:
1.杀掉生成的子线程或子进程后,主进程会一起退出
2.窗口置顶问题待解决
3.监听按键输入的功能待解决
4.自述文件的呈现
5.游戏点击速度的多级实现(最好能实时控制)(使用滑动控件)
6.音乐打开/关闭功能
7.界面调整
"""
import time
import os
import random
import threading
import ctypes
import continuous_look
import win32gui
import win32api
import win32process
from playsound import playsound  # 用于播放声音的模块
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader


class SI:
    """公共访问对象,一个界面单独创建一个类"""
    llk_window = None  # 连连看
    ttt_window = None  # 弹弹堂
    welcome_window = None  # 欢迎界面
    readme_window = None  # 自述文件


class Welcom_Window:
    """欢迎及选择游戏的界面类"""
    THE_FLAG = 1

    def __init__(self):
        """从UI文件载入已经建立好的文件样式//这是主界面模块"""

        self.window = QUiLoader().load('welcome.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.pushButton.clicked.connect(self.run_music)  # 播放声音
        # 这里需要处理音乐的打开和关闭
        self.window.pushButton_2.clicked.connect(
            self.sign_in_ttt)  # 打开弹弹堂界面的按钮
        self.window.pushButton_3.clicked.connect(
            self.sign_in_llk)  # 打开连连看界面的按钮
        self.window.action_1.triggered.connect(self.show_version)  # 版本号
        self.window.action_2.triggered.connect(self.readme)  # 自述文件
        self.window.action_3.triggered.connect(self.update)  # 更新公告
        self.window.action_4.triggered.connect(self.to_top)  # 置顶

    def sign_in_ttt(self):
        """打开弹弹堂界面"""
        SI.ttt_window = Ttt()
        self.window.hide()
        SI.ttt_window.window.show()

    def sign_in_llk(self):
        """打开连连看界面"""
        SI.llk_window = Llk()
        self.window.hide()
        SI.llk_window.window.show()

    def show_version(self):
        """展示版本号"""
        QMessageBox.information(self.window, '版本号', '语年辅助 V0.01')

    def to_top(self):
        """将界面窗口置顶"""
        pass

    def update(self):
        """更新公告"""
        QMessageBox.information(self.window, 'V0.01', '目前已经是最新版!!!')

    def readme(self):
        """打开自述文件"""
        SI.readme_window = readme_window()
        SI.readme_window.window.show()

    def run_music(self):
        self.the_threading(self.sounds)

    def sounds(cls):
        """播放或关闭背景音乐"""
        if cls.THE_FLAG == 1:
            cls.THE_FLAG = 0
            answer = os.listdir("music")  # 得到音乐文件列表
            result = random.randint(0, len(answer)-1)  # 随机播放
            path = os.path.join("music", answer[result])
            playsound(path)  # 音乐文件相对路径   (完成后需要将此行注释删除)
        else:
            return None

    def the_threading(self, aims):
        """多线程"""
        self.aims = threading.Thread(target=aims, daemon=True)  # 设置为主线程守护模式
        self.aims.start()  # 启动


class readme_window:
    """自述文件"""

    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        self.window = QUiLoader().load('readme.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.action_1.triggered.connect(self.sign_out)  # 返回主界面

    def sign_out(self):
        """返回主界面"""
        self.window.hide()
        SI.welcome_window.window.show()


class Ttt:
    """弹弹堂游戏界面的类"""

    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        self.window = QUiLoader().load('ttt.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.action_1.triggered.connect(self.sign_out)  # 返回主界面

    def sign_out(self):
        """返回主界面"""
        self.window.hide()
        SI.welcome_window.window.show()


class Llk:
    """连连看游戏界面的类"""
    THE_IMPORTANT_NUMBER = 0

    def __init__(self):
        """从UI文件获取已经建立好的文件样式"""
        self.window = QUiLoader().load('llk.ui')  # 从UI定义中动态创建一个相应的窗口对象
        self.window.pushButton.clicked.connect(self.run_game)  # 快速的
        self.window.pushButton_2.clicked.connect(self.run_game2)  # 中速的
        self.window.pushButton_3.clicked.connect(self.run_game3)  # 慢速的
        self.window.action_1.triggered.connect(self.sign_out)  # 返回主界面
        self.window.pushButton_4.clicked.connect(self.run)  # 无倒计时

    def run_game(self):
        """快速自动化执行"""
        self.the_threading(continuous_look.AutoRun.top(0.5))

    def run_game2(self):
        """快速自动化执行"""
        self.the_threading(continuous_look.AutoRun.top(0.05))

    def run_game3(self):
        """快速自动化执行"""
        self.the_threading(continuous_look.AutoRun.top(0))

    def sign_out(self):
        """返回主界面"""
        self.window.hide()
        SI.welcome_window.window.show()

    def the_threading(self, aims):
        '''多线程'''
        self.aims = threading.Thread(target=aims, daemon=True)  # 设置为主线程守护模式
        self.aims.start()  # 启动

    def run(self):
        self.the_threading(self.time_forever)

    def time_forever(self):
        """改变倒计时的内存地址的值,使其时间不减"""
        if self.THE_IMPORTANT_NUMBER == 0:
            self.THE_IMPORTANT_NUMBER = 1
            self.window_handle = win32gui.FindWindow(
                None, 'QQ游戏 - 连连看角色版')  # 获取窗口句柄
            if not self.window_handle:
                self.THE_IMPORTANT_NUMBER = 0
                return None
            else:
                self.process_id = win32process.GetWindowThreadProcessId(
                    self.window_handle)[1]  # 获取进程ID  以窗口句柄获取到的列表第一个值是线程ID,第二个值是进程ID
                self.process_handle = win32api.OpenProcess(
                    0x1F0FFF, False, self.process_id)  # 遍历所有的进程的内存地址,返回值为process_id的进程句柄
                self.kernel_32 = ctypes.windll.LoadLibrary(
                    "DLL\\kernel32.dll")  # 利用ctypes的kernel32模块往指定的内存地址里写入数据
                self.data = ctypes.c_long()
                self.kernel_32.ReadProcessMemory(
                    int(self.process_handle), 0x00186AA8, ctypes.byref(self.data), 4, None)  # 读取
                while True:
                    time.sleep(0.02)
                    self.kernel_32.WriteProcessMemory(int(self.process_handle), 0x00186AA8, ctypes.byref(
                        ctypes.c_long(750)), 4, None)  # 每0.02秒刷新地址的值
        elif self.THE_IMPORTANT_NUMBER == 1:
            return None


def main():
    """程序人口"""
    app = QApplication([])  # 创建UI对象 提供整个图形界面  从文件中加载UI定义
    SI.welcome_window = Welcom_Window()  # 实例化对象到ShareInfo
    SI.welcome_window.window.show()  # 展示窗口
    app.exec_()  # QApplication事件处理循环


if __name__ == '__main__':
    main()
