def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('相加之后的结果是:', s)
    return inner_func


ifu = func(2, 8)
ifu1 = func(3, 9)
print(ifu)
print(ifu1)
ifu()
ifu1()
