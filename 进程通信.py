from multiprocessing import Queue, Process
from time import sleep


def download(qu):
    images = ['girls.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(0.5)
        qu.put(image)


def getfile(qu):
    while True:
        try:
            file = qu.get(timeout = 5)
            print('{}保存成功！'.format(file))
        except:
            print('全部保存完毕')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


