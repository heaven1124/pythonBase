# 生成器的作用：和推导式不同，生成器不是一次性产生所有元素，而是根据需要每次产生一个元素，以便节省内存空间
# 只要函数中出现了yield关键字，函数就不是函数了，就变成了生成器
'''
步骤：
1. 定义一个函数，函数中使用yield关键字
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4.使用系统的next方法，或生成器的__next__方法得到元素
'''


def func():
    n = 0
    while True:
        n += 1
        yield n # return n + 暂停

g = func()
print(g)
print(next(g))
print(g.__next__())


# 斐波那契生成器
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:

        yield b   # return b + 暂停
        a, b = b, a + b
        n += 1
        return '没有更多元素了！！！'  # 越界后，return后的信息会当做异常抛出！


g = fib(8)
print(next(g))
print(g.__next__())
print(next(g))
print(g.__next__())