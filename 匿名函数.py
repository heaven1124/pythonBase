# r = lambda a, b: a + b
# result = r(2, 3)
# print(result)
from functools import reduce


def func(a, f):
    re = f(a)
    print(re)


func(5, lambda x: x**2)

list1 = [('tom', 12), ('olive', 18), ('candy', 15)]
s = sorted(list1, key=lambda x: x[1], reverse=True)
print(s)

rr = filter(lambda x: x[1] > 13, list1)
print(list(rr))

m = map(lambda x: x[0].title(), list1)
print(list(m))

rd = reduce(lambda x, y: x*y, [1, 2, 3, 4])
print(rd)
