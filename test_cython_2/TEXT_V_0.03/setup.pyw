# encoding = utf-8
import os
from shutil import copytree # 复制文件夹
from distutils.core import setup  # 固定写法
from Cython.Build import cythonize  # 固定写法


def setup_files():
    setup_info ="""
@echo off
pyinstaller -F _main.pyw -p _boot.pyd -p _user_login.pyd -p _window.pyd -p _run_threading.pyd -p _excel_handle.pyd -p _public.pyd --noconsole --hidden-import PySide2.QtXml --key 20210423
pause > nul

"""  # 这里可以更改要如何打包文件

    path = os.getcwd()  # 当前文件所在目录
    answer = os.listdir(path)  # 第一次遍历当前文件所在目录下的所有文件
    for i in answer:
        if i[-2:] == 'py':
            setup(name = "%s" %(i[:-4]),ext_modules = cythonize("%s" %(i)))
    result = os.listdir(path)  # 第二次遍历当前文件坐在目录下的所有文件
    os.mkdir('software')  # 创建用于放需要打包的文件的文件夹
    with open('software\\setup.bat', 'w') as f:
        f.write(setup_info)
    for i in result:
        if i[-1] == 'c':
            os.remove(i)
        if i == '_main.pyw':
            boot_path = os.path.join(path, 'software', i)
            with open(i) as f:
                temp = f.read()
            with open(boot_path, 'w') as f:
                f.write(temp)
        if os.path.isdir(i) == True and i != 'software':
            dir_path = os.path.join('software', i)  # 指定位置
            copytree(i, dir_path)  # 拷贝文件夹和其中的文件到指定位置

        if i[-3:] == 'pyd' or i[-2:] == 'ui':
            new_path = os.path.join(path, i)  # 文件路径
            with open(new_path, 'rb') as f:
                temp = f.read()
            aim_path = os.path.join(path,'software' ,i)  # 目标路径
            with open(aim_path, 'wb') as f:
                f.write(temp)
    last_answer = os.listdir(path)  # 第三次遍历当前文件坐在目录下的所有文件
    for i in last_answer:
       if i[-3:] == 'pyd':
          os.remove(i)

setup_files()
