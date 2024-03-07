import threading
import time


def fn():
    print('hello, world')


timer_1 = threading.Timer(1, fn)
timer_1.start()


def print_time():
    print(time.ctime())
    timer_2 = threading.Timer(1, print_time)
    timer_2.start()


print_time()
