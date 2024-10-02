# -*- coding: utf-8 -*-
# 遍历一个文件夹下全部C/CPP文件,并按照相同的目录格式存放在桌面的NEW文件夹下
# 目标文件夹绝对路径: r"C:\Users\Administrator.DESKTOP-PL8E08J\Desktop\NEW"

import os

def my_copy(aim_path, now_path):
	# 复制目标位置内容到目标文件夹
    files = os.listdir(now_path)
    for file in files:
        new_path = os.path.join(now_path, file)
        if os.path.isdir(new_path):
            first_path = os.path.join(aim_path, file)
            os.mkdir(first_path)
            my_copy(first_path, new_path)
        elif os.path.isfile(new_path):
            if new_path[-4:] == ".cpp" or new_path[-2:] == ".h":
                last_path = os.path.join(aim_path, file)
                with open(new_path, 'rb') as r_b:
                    temp = r_b.read()
                with open(last_path, 'wb') as w_b:
                    w_b.write(temp)

if __name__ == "__main__":
    my_copy(r"C:\Users\Administrator.DESKTOP-PL8E08J\Desktop\NEW", r"E:\study\C_X86\C_X86_2010")