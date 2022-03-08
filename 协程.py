
# 耗时操作使用协程，greenlet底层使用的是生成器，使用起来比生成器简单，不用手工调用yield
import time

from greenlet import greenlet


def a():
    for i in range(5):
        print('A' + str(i))
        gb.switch()
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.1)


def c():
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()