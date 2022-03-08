from threading import Thread

# 线程可以共享全局变量，而进程不可以
from time import sleep

ticket = 1000


def run():
    global ticket
    for i in range(100):
        sleep(0.1)
        ticket -= 1


if __name__ == '__main__':
    t1 = Thread(target=run, name='th1')
    t2 = Thread(target=run, name='th2')
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('ticket:', ticket)

