#原函数有返回值，装饰器内部函数也要有返回值
def outer(a):  #第一层，负责接收装饰器的参数
    def decorate(func):  #第二层，负责接收函数
        def wrapper(*args, **kwargs):  #第三层，负责接收函数的参数
            re = func(*args, **kwargs)
            print('预计装修费用：{}元'.format(re))
            print('刷漆')
            print('铺地板{}块'.format(a))
            print('买家具')
            print('精装修房子')
            return 60000
        return wrapper
    return decorate


@outer(99)
def house(name, address, area=40):
    print('酒店的名字是：{},酒店的地址在：{},单间面积是：{}平米'.format(name, address, area))
    return 50000


r = house(name='和平饭店', address='北京国贸')
print(r)
