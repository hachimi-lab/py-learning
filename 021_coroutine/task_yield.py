import time


def task1():
    while True:
        print("---1---")
        time.sleep(0.001)
        yield


def task2():
    while True:
        print("---2---")
        time.sleep(0.001)
        yield


t1 = task1()
t2 = task2()
while True:
    next(t1)  # 通过next()函数执行生成器
    next(t2)  # 通过next()函数执行生成器
