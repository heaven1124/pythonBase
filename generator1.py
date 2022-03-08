'''
生成器方法：
1.__next()__:生成下一个元素
2.send(value):生成下一个元素，并且每次向函数体内传值，由yield返回值接收（第一次调用必须传入None）
'''

def gen():
    i = 0
    while i < 5:
        temp = yield i  # return i + 暂停
        print('temp', temp)
        for x in range(temp):
            print('-------->', x)
        print('*************')
        i += 1
    return '没有更多数据'

g = gen()
print(g.send(None))
n1 = g.send(3)
print('n1', n1)
n2 = g.send(5)
print('n2', n2)


