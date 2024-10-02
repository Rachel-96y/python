# encoding = utf-8

import threading
class Run_Thread:
    """多线程模块创建"""
    def __init__(self, aims):
        """多线程"""
        self.aims = threading.Thread(target=aims, \
                                     daemon=True)  # 这里设置为主线程守护模式
        self.aims.start()
