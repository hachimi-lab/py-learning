"""
多进程之间数据隔离
"""
import multiprocessing
import random
import time
from datetime import datetime
from multiprocessing import Queue


def sing():
    for i in range(5):
        print("Singing")
        time.sleep(1)


def dance():
    for i in range(5):
        print("Dancing")
        time.sleep(1)


def write(_queue: Queue):
    for _ in range(5):
        time.sleep(1)
        _queue.put(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])


def read(_queue: Queue):
    for i in range(5):
        time.sleep(1)
        data = _queue.get()
        print(data)


def worker(msg):
    t_start = time.time()
    print(f"[{msg}]开始执行,进程号为{multiprocessing.current_process().pid}")
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(f"[{msg}]执行完毕，耗时{t_stop - t_start}")


if __name__ == '__main__':
    # 创建多进程
    process_1 = multiprocessing.Process(target=sing)
    process_2 = multiprocessing.Process(target=dance)
    process_1.start()
    process_2.start()
    print(multiprocessing.active_children())  # MainProcess, sing, dance
    process_1.join()
    process_2.join()

    # 通过队列实现进程之间的通信
    queue = multiprocessing.Queue()
    write_process = multiprocessing.Process(target=write, args=(queue,))
    read_process = multiprocessing.Process(target=read, args=(queue,))
    write_process.start()
    read_process.start()
    write_process.join()
    read_process.join()

    # 进程池
    pool = multiprocessing.Pool(3)
    for i in range(0, 10):
        pool.apply_async(worker, (i,))  # 进程池中的进程数为3，所以这里会先执行3个进程，然后再执行剩下的
    pool.close()
    pool.join()
