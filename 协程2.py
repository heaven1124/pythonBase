# 案例
import requests

import gevent
from gevent import monkey

monkey.patch_all()


def download(url):
    rep = requests.get(url)
    content = rep.text
    print('下载了{}的数据，长度：{}'.format(url, len(content)))


if __name__ == '__main__':
    urls = ['https://www.baidu.com', 'https://www.163.com', 'https://www.qq.com']
    g1 = gevent.spawn(download, urls[0])
    g2 = gevent.spawn(download, urls[1])
    g3 = gevent.spawn(download, urls[2])

    g1.join()
    g2.join()
    g3.join()