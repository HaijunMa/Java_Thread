'''
Title:创建一个多线程程序，分别完成100以内的奇数和以及偶数和
@author:Haijun Ma
Time:2018/9/29
'''

import threading
import time

class A(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.num = n

    def run(self):
        global num
        sum = 0
        locks.acquire()
        while True:
            if num%2 == 0:
                sum = sum + num
                time.sleep(0.1)
                if num == self.num:
                    break
                num += 1
            else:
                locks.notify()
                if num == self.num:
                    break
                locks.wait()
        print("A线程释放")
        print("100以内的偶数和：%d" % sum)
        locks.release()

class B(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.num = n

    def run(self):
        global num
        sum = 0
        locks.acquire()
        while True:
            if num%2 == 1:
                sum = sum + num
                time.sleep(0.1)
                if num == self.num:
                    break
                num += 1
            else:
                locks.notify()
                if num == self.num:
                    break
                locks.wait()
        print("B线程释放")
        print("100以内的奇数数和：%d" % sum)
        locks.release()

num = 0
locks = threading.Condition()
a = A(100)
b = B(100)
a.start()
b.start()
