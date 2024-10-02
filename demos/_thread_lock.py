import threading
import time
lock = threading.Lock()
num = [0]


def test_1():
    lock.acquire()
    for i in range(10):
        num[0] += 1
        print('第一个函数:', num)
    lock.release()


def test_2():
    lock.acquire()
    for i in range(3):
        num[0] -= 2
        print('第二个函数:', num)
    lock.release()


thread_1 = threading.Thread(target=test_1)
thread_2 = threading.Thread(target=test_2)

if __name__ == '__main__':
    thread_1.start()
    thread_2.start()
