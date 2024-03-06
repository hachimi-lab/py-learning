import threading

num = 0
mutex = threading.Lock()


def func_1(number: int):
    for i in range(number):
        if mutex.acquire():
            global num
            num += 1
            mutex.release()


def func_2(number: int):
    for i in range(number):
        if mutex.acquire():
            global num
            num += 1
            mutex.release()


thread_1 = threading.Thread(target=func_1, args=(100000000,))
thread_1.start()
thread_2 = threading.Thread(target=func_2, args=(100000000,))
thread_2.start()

thread_1.join()
thread_2.join()
print(num)
