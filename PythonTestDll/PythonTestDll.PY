#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import c_int, c_char_p, c_void_p
from win32process import GetWindowThreadProcessId, TerminateProcess
from win32api import OpenProcess
from win32gui import FindWindow, MessageBox
from win32con import *

# 用于操作窗口及相关进程的类
class CWindows:

    def __init__(self, m_Parameter_1, m_Parameter_2):
        # 构造函数
        self.m_Parameter_1 = m_Parameter_1
        self.m_Parameter_2 = m_Parameter_2
        # To do...

    def __del__(self):
        # 析构函数
        pass

    @staticmethod
    def CallBack(Function: c_void_p, Parameter_1, Parameter_2) -> c_int:
        # 回调函数
        bRet: c_int = 0
        # To do...
        x = Parameter_1 + 1
        y = Parameter_2 + 1
        z = 1000
        Function(x, y, z)
        return bRet
    
    # 杀死带有指定窗口名称的进程32/64位
    def TerminateProcByWindow(szWindowName: c_char_p) -> c_int:
        hWindow = FindWindow(NULL, szWindowName)
        if (hWindow == NULL):
            return -1
        dwPID = GetWindowThreadProcessId(hWindow)
        if(dwPID[0] == NULL): 
            return -2
        hProcess = OpenProcess(0xFFFF | 0x000F0000 | 0x00100000, NULL, dwPID[1])
        if (hProcess == NULL): 
            return -3
        bRet = TerminateProcess(hProcess, 0x1)
        if (bRet == NULL): 
            return -4

        return 0
    
def main() -> c_int:
    # 主函数
    
    dwRet = CWindows.TerminateProcByWindow("无标题 - 记事本")
    if (dwRet != NULL):
        MessageBox(0, "关闭进程失败", "失败", MB_OK)
        return FALSE
    
    return TRUE

if __name__ == "__main__":
    # main()
    print(True == 1)
    print(FALSE == 0)


r"""
hDynamic_Link = windll.LoadLibrary("..\\PythonTestDll\\Dynamic_Link.dll")
print(hDynamic_Link.Plus(1, 3))
print(hDynamic_Link.Sub(9, 3))
print(hDynamic_Link.Mul(5, 6))
print(hDynamic_Link.Div(10, 5))
"""


r"""
# import win32com.client  # 调用dll
if __name__ == "__main__":
    # 程序入口
    if getattr(sys, "frozen", False):
        # 在exe中时运行
        base_path = os.path.dirname(sys.executable)
        print(base_path)
    else:
        # 在python环境中时运行
        base_path = os.path.dirname(os.path.abspath(__file__))
        print(base_path)
    try:
        win32com.client.Dispatch("dm.dmsoft")  # 尝试调用dll
    except:
        # 这里一定会调用失败(如果要使用则需要改进)
        # 这里需要使用C语言导出一个dll来完成此功能
        pass
        # 调用失败则进行com组件注册(需要以管理员方式运行)
    finally:
        dm = win32com.client.Dispatch("dm.dmsoft")  # 获取对象以备使用
"""

# ctypes.windll.LoadLibrary(os.path.join(os.path.dirname(os.path.abspath(__file__)), "测试用DLL.dll"))