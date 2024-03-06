"""
线程之间共享全局变量
"""

import threading
import time


def sing():
    for i in range(5):
        print("Singing")
        time.sleep(1)


def dance():
    for i in range(5):
        print("Dancing")
        time.sleep(1)


# 创建线程对象
thread_sing = threading.Thread(target=sing)
thread_dance = threading.Thread(target=dance)

# 启动线程
thread_sing.start()
thread_dance.start()

print(threading.enumerate())  # MainThread, sing, dance

# 等待线程结束
thread_sing.join()
thread_dance.join()


# 定义线程类
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("MyThread")
            time.sleep(1)


my_thread = MyThread()
my_thread.start()
my_thread.join()
