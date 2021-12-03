import win32api
import win32gui
import win32con
import time
from PIL import ImageGrab
from collections import Counter
from games import SI
from PySide2.QtWidgets import QMessageBox


class AutoRun():
    """连连看游戏的类"""
    blocks_x = 19
    blocks_y = 11

    @classmethod
    def top(cls, times):
        name = 'QQ游戏 - 连连看角色版'
        hwnd = win32gui.FindWindow(None, name)
        if hwnd:
            pass
        else:
            QMessageBox.information(SI.llk_window, '失败!', '没有找到 QQ游戏 - 连连看角色版,请先打开游戏后重试!')
            return None
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.05)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        cls.rect = (left+14, top+181, left+603, top+566)
        cls.img = ImageGrab.grab().crop(cls.rect)
        AutoRun.main(times)

    @classmethod
    def shengcheng(cls):
        vaz = []  # 从0-208  一共209个方框的特征值 [[1,415,54],[2,55,56]] 这就是一个二维数组(列表)
        for y in range(cls.blocks_y):
            for x in range(cls.blocks_x):
                quare = cls.img.crop(
                    (x * 31, y * 35, (x + 1) * 31, (y + 1) * 35))
                square = quare.crop((8, 8, 25, 28))
                dian = square.getcolors()
                vaz.append(dian)
        vaz1 = vaz.copy()  # 列表对象的内置方法,相当于->  vaz1= vaz[:]
        aaa = 1
        for va in vaz:   # 这一步循环处理完成后,会得到一个对比数组以直观的体现方块是否相等
            ccc = 0
            for qa in vaz1:
                if va == qa:
                    vaz1[ccc] = aaa
                ccc += 1
            aaa = aaa+1
        xxx = Counter(vaz1)  # 得到计数每一个值个数的字典
        xz = max(zip(xxx.values(), xxx.keys()))
        iia = []
        va11 = []
        for ia in vaz1:  # 将前面的值转换成二维数组,其中值为0的是背景格
            if ia == xz[1]:  # 判断是否是背景值
                iia.append(0)
            else:
                iia.append(ia)
            if len(iia) == cls.blocks_x:
                va11.append(iia)
                iia = []
        return va11

    def hengx(x, y, x1, y1, va11):
        if y != y1:
            return False
        if x == x1:
            return False
        minx = min(x, x1)
        maxx = max(x, x1)
        # 判断纵向相邻
        if (maxx-minx) == 1:
            return True
        # 判断联通
        for i in range(minx+1, maxx):
            if va11[y][i] != 0:
                return False
        return True
    # 判断纵向

    def zongx(x, y, x1, y1, va11):
        if x != x1:
            return False
        if y == y1:
            return False
        miny = min(y, y1)
        maxy = max(y, y1)
        # 判断纵向相邻
        if (maxy-miny) == 1:
            return True
        # 判断联通
        for i in range(miny+1, maxy):
            if va11[i][x] != 0:
                return False
        return True
    # 一个拐角

    @classmethod
    def guai1(cls, x, y, x1, y1, va11):
        if x == x1 or y == y1:
            return False
        if va11[y][x1] == 0:
            if cls.zongx(x1, y, x1, y1, va11) and cls.hengx(x1, y, x, y, va11):
                return True
        if va11[y1][x] == 0:
            if cls.hengx(x, y1, x1, y1, va11) and cls.zongx(x, y1, x, y, va11):
                return True
        return False

    @classmethod
    def guai2(cls, x, y, x1, y1, va11):
        vz = []
        for yy in range(y+1, 11):
            if va11[yy][x] == 0:
                vz.append((x, yy))
            else:
                break
        for yy in range(y-1, 0, -1):
            if va11[yy][x] == 0:
                vz.append((x, yy))
            else:
                break
        for xx in range(x+1, 19):
            if va11[y][xx] == 0:
                vz.append((xx, y))
            else:
                break
        for xx in range(x-1, 0, -1):
            if va11[y][xx] == 0:
                vz.append((xx, y))
            else:
                break
        if vz == []:
            return False
        for z in vz:
            if cls.guai1(z[0], z[1], x1, y1, va11) or cls.zongx(z[0], z[1], x1, y1, va11) or cls.hengx(z[0], z[1], x1, y1, va11):
                return True
        return False

    @classmethod
    def panduan(cls, x, y, x1, y1, va11):
        if cls.zongx(x, y, x1, y1, va11):
            return True
        if cls.hengx(x, y, x1, y1, va11):
            return True
        if cls.guai1(x, y, x1, y1, va11):
            return True
        if cls.guai2(x, y, x1, y1, va11):
            return True
        return False

    @classmethod
    def dianji(cls, x, y, timing):

        win32api.SetCursorPos((x*31+15+cls.rect[0], y*35+cls.rect[1]+15))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(timing)  # 延迟   0.02 /  0.5  /  不延迟

    @classmethod
    def main(cls, timing):
        Q1 = 0
        va11 = cls.shengcheng()
        for xxxx in range(300):
            for y in range(11):
                for x in range(19):
                    if va11[y][x] == 0:
                        continue
                    for y1 in range(11):
                        for x1 in range(19):
                            if va11[y1][x1] == 0:
                                continue
                            if va11[y][x] == va11[y1][x1] and (x, y) != (x1, y1):
                                if cls.panduan(x, y, x1, y1, va11):
                                    # 鼠标点击
                                    cls.dianji(x, y, timing)
                                    cls.dianji(x1, y1, timing)
                                    va11[y][x] = 0
                                    va11[y1][x1] = 0
            if va11.count([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 11:
                return None


if __name__ == "__main__":
    pass
