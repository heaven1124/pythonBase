# 可以被next函数调用并不断返回下一个值的对象叫迭代器
# 可迭代的对象不一定是迭代器 列表，元组，字典，字符串都是可迭代的但不是迭代器
# 迭代器分二部分，一部分本身就是迭代器的一种，比如生成器；另一部分本身只是可迭代对象，不是迭代器，通过调用iter函数可以变成迭代器。
from collections import Iterable

list1 = [1, 2, 3, 4, 5]
print(isinstance(list1, Iterable))

list1 = iter(list1)  # 通过iter函数把一个可迭代的变量变成了一个迭代器

print(next(list1))
print(next(list1))