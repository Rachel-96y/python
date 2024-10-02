#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import ctypes
import platform

# 同当前Dll版本: 1.0.0.2
__version__ = "1.0.0.2"

r"""
# --------------------------------------------------------------
# 2个不同位数的dll分别对应32位和64位的python解释器
# Detect32.dll或Detect64.dll中可用的方法:
# --------------------------------------------------------------
❤  函数名:         PreventDuplicateLaunch
    作用:       防止当前程序多开, 检测到多开则退出程序
    参数:       此函数需要一个自定义的字符串类型的参数, 作为当
    前程序的唯一标志, 如果在不同程序中使用, 可能需要更改此标志
    返回值:     函数执行成功返回1, 执行失败返回0
    注意:       此函数应该在程序开始时尽早被调用
# --------------------------------------------------------------
❤  函数名:         AntiVMWare
    作用:       检测当前进程是否在VMWare虚拟机中运行
    参数:       无参
    返回值:     如果检测到VMWare虚拟机则返回1, 否则返回0
    注意:       此函数仅测试了在VMWare虚拟机中运行, 可能对其它虚拟机无效
    经测试确定: 如果在Windows中启用了SandBox沙盒则此函数也会返回1
# --------------------------------------------------------------
❤  函数名:         AntiOllyDbg
    作用:       检测当前系统进程中是否有OllyDbg调试器在运行
    参数:       无参
    返回值:     如果检测到OllyDbg调试器则返回1, 否则返回0
    注意:       此函数仅能检测OllyDbg调试器, 对其它调试器无效
# --------------------------------------------------------------
❤  函数名:         IsPortableExecutable
    作用:       检测指定路径的文件是否是32/64位可执行程序
    参数:       文件路径
    返回值:         
        -2      不是一个有效的可执行程序
        -1      文件路径不可用
        0       IsPortableExecutable函数执行失败
        1       32位可执行程序
        2       64位可执行程序
        3       未知程序
    注意:       如果是未知程序则其很可能无法正常运行
# --------------------------------------------------------------
❤  函数名:         SuspendProcessByWindow
    作用:       通过窗口名挂起进程
    参数:       窗口名称 (窗口的标题) 
    返回值:     函数执行成功返回1, 执行失败返回0
    注意:       此函数不搜索子窗口
# --------------------------------------------------------------
❤  函数名:         ResumeProcessByWindow
    作用:       通过窗口名恢复进程
    参数:       窗口名称 (窗口的标题) 
    返回值:     函数执行成功返回1, 执行失败返回0
    注意:       此函数不搜索子窗口
# --------------------------------------------------------------
❤  函数名:         TerminateProcessByWindow
    作用:       通过窗口名终止进程
    参数:       窗口名称 (窗口的标题) 
    返回值:     函数执行成功返回1, 执行失败返回0
    注意:       此函数不搜索子窗口
# --------------------------------------------------------------
❤  函数名:         QuickShutdownSystem
    作用:       执行系统快速关机
    参数:       无参
    返回值:     函数执行失败返回0
    注意:       此函数将导致系统快速关机, 请保存好重要文件后调用
# --------------------------------------------------------------
❤  函数名:         CreateSystemError
    作用:       在普通权限下抛出一个系统异常引发蓝屏
    参数:       无参
    返回值:     函数执行失败返回0
    注意:       此函数将导致蓝屏, 请保存好重要文件后调用
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

def AntiOD(hDetect):
    # 示例
    nRet = hDetect.AntiOllyDbg()
    if nRet == 0:
        print("未检测到OllyDbg调试器\n")
    else:
        print("检测到OllyDbg调试器\n")

def IsPe(hDetect):
    # 示例
    nRet = hDetect.IsPortableExecutable("C:\\Windows\\System32\\notepad.exe")
    match nRet:
        case -2:
            print("这不是一个有效的可执行程序\n")
        case -1:
            print("文件路径不可用\n")    
        case 0:
            print("IsPortableExecutable函数执行失败\n")
        case 1:
            print("这是一个32位可执行程序\n")
        case 2:
            print("这是一个64位可执行程序\n")
        case 3:
            print("未知的程序\n")

def SuspendProcess(hDetect):
    # 示例
    nRet = hDetect.SuspendProcessByWindow("无标题 - 记事本")
    if nRet == 0:
        print("SuspendProcessByWindow函数执行失败\n")
    else:
        print("SuspendProcessByWindow函数执行成功\n")

def ResumeProcess(hDetect):
    # 示例
    nRet = hDetect.ResumeProcessByWindow("无标题 - 记事本")
    if nRet == 0:
        print("ResumeProcessByWindow函数执行失败\n")
    else:
        print("ResumeProcessByWindow函数执行成功\n")

def TerminateProcess(hDetect):
    # 示例
    nRet = hDetect.TerminateProcessByWindow("无标题 - 记事本")
    if nRet == 0:
        print("TerminateProcessByWindow函数执行失败\n")
    else:
        print("TerminateProcessByWindow函数执行成功\n")

def QuickShutdown(hDetect):
    # 示例
    nRet = hDetect.QuickShutdownSystem()
    if nRet == 0:
        print("QuickShutdownSystem函数执行失败\n")

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
    AntiOD(hDetectDll)
    IsPe(hDetectDll)
    SuspendProcess(hDetectDll)
    time.sleep(5)
    ResumeProcess(hDetectDll)
    time.sleep(5)
    TerminateProcess(hDetectDll)
    # QuickShutdown(hDetectDll) #  若调用此函数成功,将快速关闭计算机
    # CreateError(hDetectDll) # 若调用此函数成功,将导致蓝屏

    os.system("pause")

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        CurrentDirectory = os.path.dirname(sys.executable)
    else:
        CurrentDirectory = sys.path[0]
    
    if platform.architecture()[0] == "32bit" and platform.system() == "Windows":
        hDetectDll = ctypes.windll.LoadLibrary(os.path.join(CurrentDirectory, "Detect32.dll"))
    elif platform.architecture()[0] == "64bit" and platform.system() == "Windows":
        hDetectDll = ctypes.windll.LoadLibrary(os.path.join(CurrentDirectory, "Detect64.dll"))
    else:
        raise Exception("PlatformError")
    main()