#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

# Powered by "阳菜"
# Version: 0.04 beta
# 此程序是用于英魂之刃人机模式的自动化挂机脚本
# 此程序为: win10 x32


"""

import os
import sys
import time
import datetime
import logging
import subprocess
import pyperclip
import pydirectinput  # 模拟键鼠事件
import threading
import win32gui
import win32con
from pynput.keyboard import Key, Listener  # 实现键盘监听
import win32com.client  # 调用dll

flags = {

    # flags为全局变量

    "flag_where_is_it": None,

    "flag_blood_pool": None,

    "flag_in_game_set_up": None,

    "flag_open_store_time": None,

    "flag_is_low_blood": None,

    "flag_soldiers_block": None,

    "flag_is_ey_towers": None,

    # 这里存储作为标志的键值对

    # 字典通过键值对赋值操作是线程安全的

}

"""

"flag_where_is_it": None
// 根据目前处于的界面设置不同的值 0 为游戏外界面 1为游戏内界面 -1为游戏结束界面

"flag_blood_pool": None
// 识别英雄是否在血池的标志 如果在血池则置为1 否则置为0

"flag_in_game_set_up": None
// 在游戏中进行设置时的标志 如果正在进行设置为1 否则置为0

"flag_open_store_time": None
// 判断此时是否可以打开商店 如果可以打开则置为1 否则置为0

"flag_is_low_blood": None
// 判断此时人物的血量是否低于健康标准 如果低于则置为1 否则置为0

"flag_soldiers_block": None
// 判断识别到的小兵的值是否低于要求 如果低于则置为1 否则置为0

"flag_is_ey_towers": None
// 判断是否有防御塔 如果有则置为1 否则置为0


"""

if 1:
    """ 常量管理 """
    DETECTION_INTERVAL: int | float = 1  # 检测窗口参数的时间间隔的常量

    COS_WINDOW_SIZE: tuple = (0, 0, 1300, 700)  # 窗口位置和大小的常量

    DARK_MOON_HUNTER: tuple = (330, 519)  # 暗月猎手英雄头像位置

    ENTER_GAME: tuple = (830, 675)  # 确定选择位置


class KeyboardMonitor(threading.Thread):

    """
    用于监听用户按键输入从而可以更好的对程序行为进行控制
    后期将做成按键退出的响应模块
    也可为之后的版本按键做准备

    """
    hwnd = win32gui.FindWindow("COSCLIENT", "英魂之刃")
    # 按下F10 开始执行脚本 按下F11 则停止

    def run(self) -> None:  # 重载run方法
        self.start_listen()

    @staticmethod
    def press(key) -> None:
        """监听键盘按下"""
        # 这里无需做任何操作
        # 响应用户的程序在按键释放后进行

        if key:
            pass

        return None

    @staticmethod
    def release(key) -> None:
        """监听键盘释放"""

        if key == Key.f11:
            win32gui.SetWindowPos(
                KeyboardMonitor.hwnd,
                win32con.HWND_NOTOPMOST,
                0,
                0,
                0,
                0,
                win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            logging.info("F11被按下,程序关闭")
            os._exit(0)
            # 退出时关闭窗口置顶

        return None

    @classmethod
    def start_listen(cls) -> None:
        """监听启动"""
        with Listener(on_press=cls.press, on_release=cls.release) as listener:
            listener.join()  # 放入线程池
        return None


class WindowProcess(threading.Thread):

    """
    处理英魂之刃游戏界面及进入人机模式游戏前的一系列操作的类
    主要操作对象为英魂之刃窗体 因脚本特殊性质 设置窗体检测间隔目前为1s

    """

    def run(self) -> None:  # 重载run方法
        self._sleep()

    @staticmethod
    def cos_handle() -> int:
        """此函数用于获取英魂之刃窗口句柄"""
        hwnd = win32gui.FindWindow("COSCLIENT", "英魂之刃")  # 窗口类名/标题
        return hwnd

    @classmethod
    def cos_window(cls) -> None:
        """获取英魂之刃窗口句柄并更改窗口位置及大小后置顶显示"""
        hwnd = cls.cos_handle()
        if hwnd == 0:  # 未启动游戏则退出程序 // 后期更改为提示
            logging.warning("未检测到英魂之刃, 程序关闭")
            os._exit(0)  # 无错误提醒退出
        flags["cos_hwnd"] = hwnd
        if win32gui.IsIconic(hwnd) == 1:  # 判断是否是最小化
            win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)  # 如果是则改为可见窗口
            logging.info("将最小化改为可见")
        else:
            pass
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE,
        )
        # 窗口置顶
        logging.info("窗口置顶")
        win32gui.MoveWindow(
            hwnd,
            COS_WINDOW_SIZE[0],
            COS_WINDOW_SIZE[1],
            COS_WINDOW_SIZE[2],
            COS_WINDOW_SIZE[3],
            True,
        )  # 更改窗口大小及位置
        logging.info("更改窗口大小及位置")
        return None

    @classmethod
    def bind_mouse_key(cls) -> None:
        """
        前/后台绑定鼠标键盘
        并关闭所绑定的窗口的输入法

        """
        hwnd = cls.cos_handle()

        if hwnd == 0:
            return None

        dm_obj.BindWindow(hwnd, "normal", "normal", "windows", 103)
        # 鼠标后台绑定需要用windows这个参数
        dm_obj.EnableIme(0)  # 关闭此句柄窗口的输入法
        return None

    @classmethod
    def is_specified_window(cls) -> bool:
        """判断英魂之刃是否以规定的大小和位置进行显示"""
        hwnd = cls.cos_handle()

        if hwnd == 0:
            logging.warning("英魂之刃已被关闭, 程序关闭")
            os._exit(0)

        if win32gui.GetWindowRect(hwnd) == COS_WINDOW_SIZE:  # (0, 0, 1300, 700)
            return 1

        else:
            return 0

    @classmethod
    def _sleep(cls) -> None:
        """在这里给检测程序做处理, 让程序每次中断1s"""
        cls.cos_window()  # 每次启动程序 这里先执行一次
        logging.info("窗口初始化完毕!")
        while True:
            hwnd = cls.cos_handle()
            if hwnd == 0:
                logging.warning("英魂之刃已被关闭, 程序关闭")
                os._exit(0)
            if cls.is_specified_window() == 1:
                # 窗口大小及位置与初始化一致则不对窗口进行操作
                pass
            else:
                cls.cos_window()  # 窗口大小及位置与初始化不一致则将其复原
                logging.info("窗口大小及位置与初始化不一致,将其复原")
                cls.bind_mouse_key()  # 绑定窗口
            time.sleep(DETECTION_INTERVAL)  # 每秒检测一次窗口状态


class AutoRun(threading.Thread):
    """
    用于自动处理在未进入游戏前的界面操作
    可自动完成: 游戏内弹窗识别并关闭 -> 进行自动匹配 -> 完成一局游戏后自动开始下一局的匹配
    此模块全部使用图片识别的方式进行处理

    """

    def run(self) -> None:  # 重载run方法
        """auto_run模块函数入口"""
        self.comprehensive()

    @classmethod
    def comprehensive(cls) -> None:
        """
        此函数协调其它函数同步工作

        """
        while True:
            time.sleep(1)
            cls.is_in_cos_game()  # 判断所处位置
            match flags["flag_where_is_it"]:
                case 0:                  # ---------<界面
                    cls.popup_process()  # 弹窗处理
                    cls.interface()      # 进入游戏
                    cls.enter_game()     # 选人界面
                case 1:                  # ---------<游戏中
                    cls.check_shopping()  # 检测是否正常关闭商店
                case -1:                 # ---------<游戏结束
                    cls.back_lobby()     # 返回界面
                case _:
                    pass      # 如果出现其它情况则让程序继续向下执行

    @staticmethod
    def is_in_cos_game() -> None:
        """
        此函数判断是否在人机模式游戏中
        游戏界面 flags["flag_where_is_it"] 值更改为 0
        在游戏中 flags["flag_where_is_it"] 值更改为 1
        游戏结束 flags["flag_where_is_it"] 值更改为 -1

        """
        AutoRun.warning()        # 检测是否有挂机警告
        result_1 = dm_obj.FindPic(  # 是否在游戏中
            808,
            665,
            847,
            684,
            "%s\\store.bmp" % image_path,
            "101010",
            0.98,
            1,
        )
        if result_1[0] != -1:
            flags["flag_where_is_it"] = 1
            return
        result_2_1 = dm_obj.FindPic(  # 是否在游戏结束界面_1
            597,
            504,
            704,
            539,
            "%s\\end_game.bmp" % image_path,
            "101010",
            0.98,
            1,
        )
        result_2_2 = dm_obj.FindPic(  # 是否在游戏结束界面_2
            1005,
            662,
            1110,
            689,
            "%s\\back.bmp" % image_path,
            "101010",
            0.98,
            1,
        )
        if result_2_1[0] != -1 or result_2_2[0] != -1:
            flags["flag_where_is_it"] = -1
            return

        flags["flag_where_is_it"] = 0  # 否则在游戏界面
        return None

    @staticmethod
    def popup_process() -> None:
        """ 此函数用于处理游戏内的弹窗 """
        result_1 = dm_obj.FindPic(  # 活动弹窗_1
            972,
            108,
            1060,
            188,
            "%s\\advertisement_1.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_1[0] != -1:
            logging.info("关闭活动弹窗_1")
            dm_obj.MoveTo(result_1[1] + 5, result_1[2] + 5)
            dm_obj.LeftClick()

        result_2 = dm_obj.FindPic(  # 活动弹窗_2(邀请参与游戏弹窗)
            948,
            82,
            1079,
            196,
            "%s\\advertisement_2.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_2[0] != -1:
            logging.info("关闭邀请参与游戏弹窗")
            dm_obj.MoveTo(result_2[1] + 5, result_2[2] + 5)
            dm_obj.LeftClick()
        return None

    @staticmethod
    def interface() -> None:
        result_1 = dm_obj.FindPic(  # 人机匹配
            771,
            104,
            853,
            145,
            "%s\\human_machine.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_1[0] != -1:
            logging.info("进入人机匹配")
            dm_obj.MoveTo(result_1[1], result_1[2])
            dm_obj.LeftClick()

        result_2 = dm_obj.FindPic(  # 开始匹配
            672,
            437,
            703,
            458,
            "%s\\matching_interface.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_2[0] != -1:
            logging.info("点击开始匹配")
            dm_obj.MoveTo(result_2[1], result_2[2])
            dm_obj.LeftClick()

        result_3 = dm_obj.FindPic(  # 接受匹配
            522,
            403,
            652,
            475,
            "%s\\accept.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_3[0] != -1:
            logging.info("点击接受匹配")
            dm_obj.MoveTo(result_3[1], result_3[2])
            dm_obj.LeftClick()

        result_3_1 = dm_obj.FindPic(  # 66放肆嗨识别扩充
            522,
            403,
            652,
            475,
            "%s\\accept_1.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_3_1[0] != -1:
            logging.info("点击接受匹配(66放肆嗨识别扩充)")
            dm_obj.MoveTo(result_3_1[1], result_3_1[2])
            dm_obj.LeftClick()

    @staticmethod
    def enter_game() -> None:
        """ 在选人界面进行选人的操作 """
        result_1 = dm_obj.FindPic(  # 搜索框放大镜位置
            949,
            457,
            1012,
            509,
            "%s\\input.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        if result_1[0] != -1:
            logging.info("识别搜索框放大镜位置")
            dm_obj.MoveTo(result_1[1] - 80, result_1[2] + 5)
            dm_obj.LeftClick()
            logging.info("点击搜索框")
            pyperclip.copy("ayl")
            pydirectinput.keyDown("ctrl")
            pydirectinput.keyDown("v")
            pydirectinput.keyUp("v")
            pydirectinput.keyUp("ctrl")
            logging.info("粘贴ayl")
            dm_obj.MoveTo(DARK_MOON_HUNTER[0], DARK_MOON_HUNTER[1])  # 英雄头像
            dm_obj.LeftClick()
            dm_obj.MoveTo(ENTER_GAME[0], ENTER_GAME[1])  # 确定选择
            dm_obj.LeftClick()
            logging.info("点击英雄头像")
        return None   # 确定选择后就不会再出现放大镜图案

    @staticmethod
    def back_lobby() -> None:
        """ 一局游戏结束后返回大厅 """
        result_1 = dm_obj.FindPic(  # 是否在游戏结束界面_1
            597,
            504,
            704,
            539,
            "%s\\end_game.bmp" % image_path,
            "101010",
            0.98,
            1,
        )
        if result_1[0] != -1:
            logging.info("返回大厅界面_1")
            dm_obj.MoveTo(651, 521)
            dm_obj.LeftClick()
            time.sleep(3)

        result_2 = dm_obj.FindPic(  # 是否在游戏结束界面_2
            1005,
            662,
            1110,
            689,
            "%s\\back.bmp" % image_path,
            "101010",
            0.98,
            1,
        )
        if result_2[0] != -1:
            logging.info("返回大厅界面_2")
            # 将所有值初始化
            flags["flag_where_is_it"] = None
            flags["flag_blood_pool"] = None
            flags["flag_in_game_set_up"] = None
            flags["flag_open_store_time"] = None
            flags["flag_is_low_blood"] = None
            flags["flag_soldiers_block"] = None
            flags["flag_is_ey_towers"] = None

            dm_obj.MoveTo(1057, 676)
            dm_obj.LeftClick()
        return None

    def warning() -> None:
        """ 用于关闭游戏中系统挂机警告"""
        result_1 = dm_obj.FindPic(
            598,
            398,
            704,
            428,
            "%s\\i_agree.bmp" % image_path,
            "050505",
            0.98,
            0,
        )  # "我同意"的按钮
        if result_1[0] != -1:
            logging.warning("人物未进行操作,关闭游戏中系统挂机警告")
            dm_obj.MoveTo(652, 411)
            dm_obj.LeftClick()

    def check_shopping() -> None:
        """ 用于关闭没有正确关闭的商店"""
        if flags["flag_where_is_it"] == 1 and flags["flag_open_store_time"] == 2:
            result_1 = dm_obj.FindPic(
                951,
                104,
                983,
                138,
                "%s\\close_store.bmp" % image_path,
                "050505",
                0.98,
                0,
            )  # 判断是否商店被打开

            if result_1[0] != -1:  # 如果被打开则关闭商店
                logging.warning("未正确关闭商店,重新关闭")
                dm_obj.MoveTo(966, 119)
                dm_obj.LeftClick()


class DarkMoonHunter():

    """
    # 专用于暗月猎手的类
    # 后期在进入游戏前需要先将要用到的图片加载进内存以提高运行速率
    # 此后可能继承或重构此类来更新其它英雄
    # 默认为用户选取了大家都有的暗月猎手

    """

    @staticmethod
    def get_red_s() -> None:
        """
        获取屏幕上敌方小兵的位置
        A键攻击小兵

        """
        result = dm_obj.FindPic(
            16,
            55,
            1251,
            614,
            "%s\\red_s.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        # 匹配和敌方血条相似的图片 相似度0.98
        # 返回值result是一个元组

        if result[0] != -1:  # 值不为-1则识别到了相似图片
            dm_obj.MoveTo(result[1] + 25, result[2] + 25)  # 精确点击
            pydirectinput.press("a")
            dm_obj.LeftClick()
        return None

    @staticmethod
    def get_red_s_ex() -> tuple:
        """
        此函数的返回值有两个:
        第一个值是整形:代表范围内的敌方士兵数量
        第二个值是一个列表:其内部是元组
        元组的两个参数代表敌方小兵在屏幕上的坐标(这里不区分是哪一个士兵)
        此函数用于判断在什么时候释放技能以及往什么方向释放技能

        """
        result = dm_obj.FindPicEx(
            16,
            55,
            1251,
            614,
            "%s\\red_s.bmp" % image_path,
            "050505",
            0.98,
            1,
        )

        if result == "":
            return 0, None

        else:
            num = result.count("|")
            ret_num = num + 1  # 敌方数量等于 "|" 的数量加1
            result = result.replace(" ", "")
            red_s_quantity = result.split("|")
            # 注意red_s_quantity里面的每一个元素 还是字符串str
            aim_list = []
            list_location = []

            for i in red_s_quantity:  # i："0,100,20"
                i = i.split(",")

                for j in i:
                    j = int(j)  # 类型强转
                    aim_list.append(j)  # 此时还剩一个列表 值全为整形

            for key, value in enumerate(aim_list):  # 0值作为分隔符

                if value == 0:
                    int_x = key + 1
                    int_y = key + 2
                    list_location.append((aim_list[int_x], aim_list[int_y]))
                    # 得到int_x, int_y坐标并放入列表list_location

            return ret_num, list_location

    @staticmethod
    def get_low_blood_red_s() -> None:
        """
        获取屏幕上敌方残血小兵的位置
        (目前：残血英雄也可能被获取到 后面的版本需要改进此问题)
        并右键攻击小兵

        """
        result = dm_obj.FindPic(
            16,
            55,
            1251,
            614,
            "%s\\low_blood_red_s.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        # 这个范围不是全屏,距离基本等于暗月攻击距离
        # 这个函数目前有一定的识别率但不是很高

        if result[0] != -1:
            dm_obj.MoveTo(result[1] + 25, result[2] + 25)
            pydirectinput.press("a")
            dm_obj.LeftClick()
        return None

    @staticmethod
    def ey_towers() -> None:
        """
        识别敌方防御塔
        并对塔进行攻击
        并改变全局变量flags[""] 的值使得在塔下的时候
        英雄不会对对方英雄造成伤害

        """
        result = dm_obj.FindPic(
            16,
            55,
            1251,
            614,
            "%s\\tower_blood.bmp" % image_path,
            "050505",
            0.98,
            0,
        )

        if result[0] == -1:
            # 没有塔
            flags["flag_is_ey_towers"] = 0  # 值置为0

        else:  # 有塔
            flags["flag_is_ey_towers"] = 1  # 有塔则值置为1
            dm_obj.MoveTo(result[1] + 50, result[2] + 100)
            dm_obj.RightClick()
        return None

    @staticmethod
    def ey_hero() -> list:
        """
        识别敌方英雄 
        并攻击英雄
        返回值为敌方英雄坐标

        """
        result = dm_obj.FindPic(
            16,
            55,
            1251,
            614,
            "%s\\red_hero_blood.bmp" % image_path,
            "050505",
            0.98,
            1,
        )

        if result[0] != -1 and flags["flag_is_ey_towers"] == 0:
            dm_obj.MoveTo(result[1] + 50, result[2] + 50)
            pydirectinput.press("a")
            dm_obj.LeftClick()

        return result

    @staticmethod
    def our_hero() -> list:
        """
        识别友方英雄 
        不存在则返回-1

        """
        result = dm_obj.FindPic(
            755,
            26,
            1200,
            325,
            "%s\\our_hero_blood.bmp" % image_path,
            "050505",
            0.98,
            1,
        )
        return result

    @staticmethod
    def get_green_s() -> list:
        """识别友方小兵并返回坐标"""
        result = dm_obj.FindPic(
            16,
            55,
            1251,
            614,
            "%s\\green_s.bmp" % image_path,
            "050505",
            0.98,
            2,
        )
        if result[0] != -1:
            return result

    @staticmethod
    def get_green_s_ex() -> tuple:
        """识别范围内友方小兵数量"""
        # 这里需要改一下变量名称
        result = dm_obj.FindPicEx(
            469,
            34,
            1268,
            593,
            "%s\\green_s.bmp" % image_path,
            "050505",
            0.98,
            2,
        )
        if result == "":
            return 0, None

        else:
            num = result.count("|")
            ret_num = num + 1  # 小兵数量等于 "|" 的数量加1
            result = result.replace(" ", "")
            red_s_quantity = result.split("|")
            # 注意red_s_quantity里面的每一个元素 还是字符串str
            aim_list = []
            list_location = []

            for i in red_s_quantity:  # i："0,100,20"
                i = i.split(",")

                for j in i:
                    j = int(j)  # 类型强转
                    aim_list.append(j)  # 此时还剩一个列表 值全为整形

            for key, value in enumerate(aim_list):  # 0值是没有意义的 将其作为分隔符

                if value == 0:
                    int_x = key + 1
                    int_y = key + 2
                    list_location.append((aim_list[int_x], aim_list[int_y]))
                    # 得到int_x, int_y坐标并放入列表list_location

            return ret_num, list_location

    @staticmethod
    def add_skills() -> None:
        """人物自动加技能"""
        result_1 = dm_obj.FindPic(
            498,
            550,
            708,
            594,
            "%s\\skills_1.bmp" % image_path,
            "050505",
            0.98,
            3,
        )
        result_2 = dm_obj.FindPic(
            498,
            550,
            708,
            594,
            "%s\\skills_2.bmp" % image_path,
            "050505",
            0.98,
            3,
        )

        if result_1[0] != -1:
            dm_obj.MoveTo(result_1[1] + 10, result_1[2] + 10)
            dm_obj.LeftClick()
            return

        if result_2[0] != -1:
            dm_obj.MoveTo(result_2[1] + 10, result_2[2] + 10)
            dm_obj.LeftClick()
            return
        return None

    @staticmethod
    def use_skills(cls):
        """人物使用技能"""
        # 此函数后期还需要判断是否技能在CD  -------------------<<
        # 这里需要通过存放的图片判断对方小兵和英雄
        enemy_information = cls.get_red_s_ex()
        if enemy_information[0] >= 2:  # 敌方数量小于2个则不做操作

            result_1 = dm_obj.FindPic(
                618,
                596,
                654,
                637,
                "%s\\skill_e.bmp" % image_path,
                "050505",
                0.98,
                0,
            )  # 判断技能是否在冷却中

            if result_1[0] != -1:
                pydirectinput.press("e")
                # 查找敌方小兵的范围 304, 145, 934, 604
                center_point = cls.get_red_s_center_point(enemy_information)
                dm_obj.MoveTo(center_point[0], center_point[1])
                dm_obj.LeftClick()

        is_hero = cls.ey_hero()  # 判断是否是英雄

        if is_hero[0] != -1:

            # 是敌方英雄则可以放大招
            result_2 = dm_obj.FindPic(
                662,
                601,
                696,
                637,
                "%s\\skill_r.bmp" % image_path,
                "050505",
                0.98,
                0
            )

            if result_2[0] != -1:
                pydirectinput.press("r")
                dm_obj.MoveTo(is_hero[1] + 50, is_hero[2] + 50)
                # 这里偏移值为50, 50 刚好可以锁定到英雄身上
                dm_obj.LeftClick()

    @staticmethod
    def get_red_s_center_point(red_s_ex_location) -> tuple:
        """
        此函数接受的参数是一个整数和一个列表 (n, [(a, b), (c, d), (e, f)...])
        列表内部是元组 数量为任意多个 元素个数大于等于3
        每个元组的两个值分别代表一个士兵的int_x和int_y坐标
        此函数计算敌方所有小兵(小兵在3个以上时)的中心点
        此函数返回值是一个元组(int_x, int_y)

        """
        sum_list_x = []
        sum_list_y = []

        for i in red_s_ex_location[1]:  # 将x坐标和y坐标分别放入不同的列表
            sum_list_x.append(i[0])
            sum_list_y.append(i[1])
        sum_list_x = sum(sum_list_x)
        sum_list_y = sum(sum_list_y)
        center_point = (
            sum_list_x / red_s_ex_location[0],
            sum_list_y / red_s_ex_location[0],
        )  # 得到中心点p
        return center_point

    def move() -> None:
        """
        此函数判断血量是否低于指定标准
        并进行人物移动

        """
        while 1:
            time.sleep(1)
            while flags["flag_where_is_it"] == 1 and flags["flag_in_game_set_up"] == 0:
                logging.info("move 正常运行")
                time.sleep(0.5)
                result_1 = dm_obj.FindPic(
                    506,
                    653,
                    607,
                    665,
                    "%s\\mine_low_blood.bmp" % image_path,
                    "050505",
                    0.98,
                    2,
                )  # 判断是否血量低于指定标准

                if result_1[0] != -1:  # 找得到图片证明血量健康
                    flags["flag_is_low_blood"] = 0  # 血量健康值置为0

                    if flags["flag_blood_pool"] == 1:  # 如果在血池
                        time.sleep(1)  # 这个时间是给买装备用的
                        dm_obj.MoveTo(86, 617)  # 己方高台的位置
                        time.sleep(0.5)
                        dm_obj.RightClick()

                    elif flags["flag_blood_pool"] == 0:  # 不在血池 则判断是否有己方小兵
                        answer_1 = DarkMoonHunter.get_green_s_ex()
                        answer_2 = DarkMoonHunter.our_hero()

                        if answer_1[0] <= 2 and answer_2[0] == -1:  # 当小于或等于2个小兵时就撤退
                            flags["flag_soldiers_block"] = 1
                            dm_obj.MoveTo(86, 617)
                            dm_obj.RightClick()
                            time.sleep(1)
                        else:
                            flags["flag_open_store_time"] = 2  # 暂时的值 原本为1
                            flags["flag_soldiers_block"] = 0
                            red_s_location = DarkMoonHunter.get_green_s()
                            if red_s_location == None:
                                pass
                            else:
                                dm_obj.MoveTo(
                                    red_s_location[1] + 25, red_s_location[2] + 25)
                                dm_obj.RightClick()
                                time.sleep(1)

                else:
                    flags["flag_is_low_blood"] = 1  # 血量不健康
                    while flags["flag_where_is_it"] == 1:
                        dm_obj.MoveTo(24, 678)  # 血池定位点
                        time.sleep(0.2)
                        dm_obj.RightClick()
                        time.sleep(1)

                        if flags["flag_blood_pool"] == 1:  # 回到血池
                            result_2 = dm_obj.FindPic(
                                683,
                                652,
                                734,
                                682,
                                "%s\\mine_hight_blood.bmp" % image_path,  # 血量回满
                                "050505",
                                0.98,
                                2,
                            )

                            if result_2[0] != -1:
                                break

    def shopping() -> None:
        """
        # 购买商品
        # 判断自己是否在商店附近
        # 每次回家只能开启一次商店并购买一次物品

        """
        while 1:
            time.sleep(1)
            while (
                    flags["flag_where_is_it"] == 1
                and flags["flag_in_game_set_up"] == 0
                and flags["flag_open_store_time"] == 1
            ):
                logging.info("shopping 正常运行")
                if flags["flag_blood_pool"] != 1:  # 不在血池不进行操作
                    time.sleep(1)
                    continue
                # 需要在游戏内 且游戏设置完成后 且商店锁值为1的情况下
                flags["flag_in_game_set_up"] = 1  # 再将这个值置为1 直到买完东西
                time.sleep(0.5)
                dm_obj.MoveTo(827, 673)  # 找到人物界面商店图标
                time.sleep(0.5)
                dm_obj.LeftClick()
                # 选择并购买没有拥有的并且可买的装备
                time.sleep(0.5)
                pic_location_str = dm_obj.FindPicEx(
                    465,
                    163,
                    672,
                    198,
                    "%s\\equipment_1.bmp | \
                     %s\\equipment_2.bmp | \
                     %s\\equipment_3.bmp | \
                     %s\\equipment_4.bmp | \
                     %s\\equipment_5.bmp | \
                     %s\\equipment_6.bmp |"
                    % (image_path,
                       image_path,
                       image_path,
                       image_path,
                       image_path,
                       image_path,),
                    "050505",
                    0.98,
                    1,
                )
                # 返回值形式: "0,100,20|2,30,40" -> str
                # 需要得到的值: (int_x, int_y)

                if pic_location_str == "":
                    # 如果没有商品可以买
                    time.sleep(0.5)
                    dm_obj.MoveTo(966, 119)  # 关闭商店
                    time.sleep(0.5)
                    dm_obj.LeftClick()
                    flags["flag_open_store_time"] = 2  # 暂时的值 原本为0
                    flags["flag_in_game_set_up"] = 0

                else:
                    pic_location_str = pic_location_str.replace(
                        " ", "")  # 去除空格
                    pic_quantity = pic_location_str.split(
                        "|")  # 以"|"拆分字符串并将其放入列表
                    # 注意pic_quantity里面的每一个元素 还是字符串str
                    # [("0,100,20"),("0,30,40"),("0,60,70")]
                    max_list = []
                    aim_list_pic = (
                        []
                    )  # [4,100,20,1,30,40,4,60,70,5,100,20,6,30,40,7,60,70]
                    list_location_pic = (
                        []
                    )  # list_location_pic = [(2 , 234, 234) , (4 , 234, 234)]

                    for i in pic_quantity:  # i："0,100,20"
                        i = i.split(",")

                        for j in i:
                            j = int(j)  # 类型强转
                            aim_list_pic.append(j)  # 此时还剩一个列表 值全为整形

                    for key, value in enumerate(aim_list_pic):

                        if (
                            value == 0
                            or value == 1
                            or value == 2
                            or value == 3
                            or value == 4
                            or value == 5
                        ):
                            int_x = key + 1
                            int_y = key + 2
                            list_location_pic.append(
                                (value, aim_list_pic[int_x],
                                 aim_list_pic[int_y])
                            )
                            # 得到int_x, int_y坐标并放入列表list_location_pic

                    for x in list_location_pic:
                        max_list.append(x[0])
                    answer = max(max_list)  # 从商店买 钱够的 最右边的东西

                    for y in list_location_pic:

                        if y[0] == answer:
                            dm_obj.MoveTo(y[1], y[2])
                            time.sleep(0.5)
                            dm_obj.RightClick()
                            break

                    time.sleep(0.5)
                    dm_obj.MoveTo(966, 119)  # 关闭商店
                    time.sleep(0.5)
                    dm_obj.LeftClick()
                    time.sleep(1)
                    flags["flag_open_store_time"] = 2  # 暂时的值 原本为0
                    flags["flag_in_game_set_up"] = 0

    def is_in_blood_pool() -> None:
        """判断是否在血池"""
        while 1:
            time.sleep(1)
            while flags["flag_where_is_it"] == 1 and flags["flag_in_game_set_up"] == 0:
                logging.info("is_in_blood_pool 正常运行")
                time.sleep(1)
                result = dm_obj.FindPic(
                    123,
                    12,
                    654,
                    552,
                    "%s\\boss.bmp" % image_path,
                    "050505",
                    0.98,
                    1,
                )

                if result[0] == -1:  # 不在血池
                    time.sleep(1)

                    if flags["flag_blood_pool"] != 0:
                        flags["flag_blood_pool"] = 0

                elif result[0] != -1:  # 在血池
                    time.sleep(1)

                    if flags["flag_blood_pool"] != 1:
                        flags["flag_blood_pool"] = 1

    def start_more() -> None:
        """
        暗月猎手部分函数综合调用启动

        """
        while 1:
            time.sleep(1)
            flags["flag_is_ey_towers"] = 0  # 先将这个值放入
            while (
                    flags["flag_where_is_it"] == 1      # 在游戏中
                and flags["flag_in_game_set_up"] == 0   # 设置完成后
                and flags["flag_is_low_blood"] == 0     # 不是低血量
                and flags["flag_soldiers_block"] == 0   # 附近有2个或以上小兵存在
                and flags["flag_is_ey_towers"] == 0     # 没有敌方防御塔的情况下
            ):
                time.sleep(0.2)
                DarkMoonHunter.ey_towers()
                logging.info("ey_towers 正常运行")
                if flags["flag_is_ey_towers"] != 0:
                    continue
                DarkMoonHunter.get_red_s()
                logging.info("get_red_s 正常运行")
                DarkMoonHunter.get_low_blood_red_s()
                logging.info("get_low_blood_red_s 正常运行")
                DarkMoonHunter.add_skills()
                logging.info("add_skills 正常运行")
                DarkMoonHunter.use_skills(DarkMoonHunter)
                logging.info("use_skills 正常运行")

    def in_game_settings() -> None:
        """
        英魂之刃人机模式 如果在设置中勾选了镜头跟随并点击确认后
        在本局游戏中会生效 但是进入下一把游戏后还需要点击确认按钮
        因英魂之刃设置界面大小保持不变 故直接按键点击指定位置

        """
        while 1:
            time.sleep(1)
            while (
                flags["flag_where_is_it"] == 1 and flags["flag_in_game_set_up"] == None
            ):
                logging.info("in_game_settings 正常运行")
                flags["flag_in_game_set_up"] = 1  # 首先将值置为1 防止其它协程运行
                # ------------------------------------------------<<开始设置
                time.sleep(0.3)
                dm_obj.MoveTo(1238, 26)  # 右上角设置按钮
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(651, 260)  # 游戏设置
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(550, 126)  # 找到游戏内设置
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(233, 593)  # 默认设置
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(396, 202)  # 镜头跟随
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(578, 203)  # 镜头跟随修正
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(763, 204)  # 血量报警
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(219, 231)
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(455, 123)  # 界面设置
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(233, 593)  # 默认设置
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(646, 596)  # 确定按钮
                time.sleep(0.3)
                dm_obj.LeftClick()
                time.sleep(0.3)
                dm_obj.MoveTo(214, 628)  # 左下角小地图缩放按钮
                time.sleep(0.3)
                dm_obj.LeftClick()
                # ------------------------------------------------<<设置完毕
                time.sleep(0.3)
                dm_obj.MoveTo(24, 678)  # 移动到血池指定点
                time.sleep(0.3)
                dm_obj.RightClick()
                time.sleep(0.3)
                flags["flag_open_store_time"] = 1  # 商店锁 值置为1
                flags["flag_in_game_set_up"] = 0  # 值等于0代表设置完毕


def main() -> int:
    """ 
    主函数 
    由主线程创建子线程并统一管理

    """
#   ------------------------------------------< 游戏外
    thread_1 = WindowProcess()  # 实例化窗口检测线程
    logging.info("实例化窗口检测线程")
    thread_2 = AutoRun()  # 实例化界面操作线程
    logging.info("实例化界面操作线程")

    thread_1.start()
    thread_2.start()

    thread_3 = KeyboardMonitor()  # 实例化键盘监听线程
    logging.info("实例化键盘监听线程")
    thread_3.start()

#   ------------------------------------------< 游戏中
    thread1 = threading.Thread(
        target=DarkMoonHunter.in_game_settings)  # 游戏内设置
    logging.info("启动游戏设置线程")
    thread2 = threading.Thread(
        target=DarkMoonHunter.is_in_blood_pool)  # 血量判断
    logging.info("启动血量判断线程")
    thread3 = threading.Thread(target=DarkMoonHunter.shopping)    # 购买物品
    logging.info("启动购买物品线程")
    thread4 = threading.Thread(target=DarkMoonHunter.move)    # 人物移动
    logging.info("启动人物移动线程")
    thread5 = threading.Thread(target=DarkMoonHunter.start_more)  # 人物其它行为
    logging.info("启动人物其它行为线程")

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    return 0


if __name__ == "__main__":
    # 程序入口
    if getattr(sys, "frozen", False):
        # 在exe中时运行
        base_path = os.path.dirname(sys.executable)
    else:
        # 在python环境中时运行
        base_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists("%s\\logs" % base_path) == True:  # 检验文件夹是否存在
        pass
    else:
        os.mkdir("logs")  # 不存在则重新创建 防止出现异常
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day
    logging.basicConfig(
        filename="%s\\logs\\%d-%d-%d.txt" % (base_path, year, month, day), # 文件路径
        filemode="a",       # 追加模式
        level=logging.DEBUG,    # 提示等级
        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s")
    # 日志格式
    # logging.disable(logging.DEBUG)
    # logging.disable(logging.INFO)
    # logging.disable(logging.WARNING)
    # logging.disable(logging.ERROR)
    # logging.disable(logging.CRITICAL)  # 设置logging警告阈值

    logging.info("-------------------> 程序启动 <-------------------")
    try:
        logging.info("正在尝试调用com组件...")
        win32com.client.Dispatch("dm.dmsoft")  # 尝试调用dll
    except:
        logging.warning("调用com组件失败...")
        logging.warning("尝试注册com组件到系统...")
        subprocess.run("regsvr32 /s %s\\dm.dll" % os.path.join(base_path, "bin"), shell=True,
                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 调用失败则进行com组件注册(需要以管理员方式运行)
    finally:
        dm_obj = win32com.client.Dispatch("dm.dmsoft")  # 获取对象以备使用
        logging.info("组件注册或调用成功,程序正常运行...")
        image_path = os.path.join(base_path, "image")   # 拼接得到image文件夹路径
    main()
