import time
from multiprocessing import Pool
from random import random
from time import sleep


def task1(task_name):
    print('task begin' + task_name)
    time.sleep(random()*2)
    return 'finish task---------' + task_name


def call_back(n):
    print(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['洗衣服', '做饭', '接孩子', '扫地', '擦玻璃', '倒垃圾']
    for i in tasks:
        pool.apply_async(task1, args=(i,), callback=call_back)

    pool.close()
    pool.join()  # 挡住主进程不让主进程结束，因为使用进程池的时候一旦主进程结束子进程也会结束

