#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import ctypes
import platform

r"""
# --------------------------------------------------------------
# 2个版本的dll分别对应32位和64位的python解释器
# Detect32.dll或Detect64.dll中可用的方法:
# --------------------------------------------------------------
❤  函数名:         PreventDuplicateLaunch
    作用:       防止当前程序多开, 检测到多开则退出程序
    参数:       此函数需要一个自定义的字符串类型的参数, 作为当
    前程序的唯一标志, 如果在不同程序中使用, 可能需要更改此标志
    返回值:     函数执行成功返回1, 否则返回0
    注意事项:   此函数应该在程序开始时尽早被调用
# --------------------------------------------------------------
❤  函数名:         AntiVMWare
    作用:       检测当前进程是否在VMWare虚拟机中运行
    参数:       无参
    返回值:     如果检测到虚拟机则返回1, 否则返回0
    注意事项:   此函数仅能检测VMWare虚拟机, 对其它虚拟机无效
# --------------------------------------------------------------
❤  函数名:         CreateSystemError
    作用:       在普通权限下抛出一个系统异常引发蓝屏 
    参数:       无参 
    返回值:     函数执行成功返回1, 执行失败返回0
    注意事项:   此函数将可能导致蓝屏, 请保持重要文件后调用
# --------------------------------------------------------------
"""

def PreventDuplicateRun(hDetect):
    # 示例
    nRet = hDetect.PreventDuplicateLaunch("EXAMPLE_FLAG")
    if nRet == 0:
        print("\nPreventDuplicateLaunch函数执行失败\n")
    else:
        print("\nPreventDuplicateLaunch函数执行成功\n")

def AntiVM(hDetect):
    # 示例
    nRet = hDetect.AntiVMWare()
    if nRet == 0:
        print("未检测到VMWare虚拟机\n")
    else:
        print("检测到VMWare虚拟机\n")

def CreateError(hDetect):
    # 示例
    nRet = hDetect.CreateSystemError()
    if nRet == 0:
        print("CreateSystemError函数执行失败\n")

# --------------------------------------------------------------

def main():
    # 调用
    PreventDuplicateRun(hDetectDll)
    AntiVM(hDetectDll)
    # CreateError(hDetectDll) # 若调用此函数成功,可能将导致蓝屏

    os.system("pause")

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        CurrentDirectory = os.path.dirname(sys.executable)
    else:
        CurrentDirectory = sys.path[0]
    if platform.architecture()[0] == "32bit" and platform.system() == "Windows":
        hDetectDll = ctypes.windll.LoadLibrary(os.path.join(CurrentDirectory, "Detect32.dll"))
    else:
        hDetectDll = ctypes.windll.LoadLibrary(os.path.join(CurrentDirectory, "Detect64.dll"))
    main()