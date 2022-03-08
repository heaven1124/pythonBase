# gevent中封装了greenlet，遇到耗时操作能够实现协程任务的自动切换
import time

import gevent
from gevent import monkey


monkey.patch_all()  # 把程序中所有的普通sleep方法换成gevent中的sleep方法，以便程序能够自动感知到sleep耗时操作，然后自动swich协程任务


def a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


def c():
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()