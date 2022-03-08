import queue
from multiprocessing import Process
from time import sleep
import os


def task1(s):
    while True:
        sleep(s)
        print('this is task1-------', os.getpid(), '------', os.getppid())


def task2(s):
    while True:
        sleep(s)
        print('this is task2---------', os.getpid(), '------', os.getppid())


if __name__ == '__main__':

    print(os.getpid())
    p1 = Process(target=task1, args=(1,))
    p1.start()
    p2 = Process(target=task2, args=(2,))
    p2.start()
    sleep(2)
    p1.terminate()
    p2.terminate()

