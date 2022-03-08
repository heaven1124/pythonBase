import random

a = [x for x in range(1, 101)]
b = [a[i:i+3] for i in range(0, len(a), 3)]
print(b)

names = [['Tom', 'Jefferson', 'Mary', 'Wesley', 'Joe', 'Olive'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Eva']]
new_names = [j for i in names for j in i if j.count('e')>=2]
print(new_names)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [y+2 if y % 2 == 0 else y+1 for y in list1]


# 字典推导式 {key,value for k,v in 字典.items()}
class User():
    id = 2
    name = 'sl'


user = User()
user.id = 23
user.name = 'shilei'
print(user.__dict__)
print({attr: getattr(user, attr) for attr in dir(user) if not attr.startswith('__')})

# 根据对象自动生成sql语句
def save(entity):
    sql = "insert into %s(%s) values (%s)"
    table = entity.__class__.__name__.lower()
    colnames = ','.join([col for col in entity.__dict__])
    colplaceholder = ','.join(["%%(%s)s" % col for col in entity.__dict__])

    sql = sql % (table, colnames, colplaceholder)
    print(sql)

#随机生成20位小写字母和数字组合
def generate():
    lst = [chr(i) for i in range(97, 97+26)] + [str(i) for i in range(10)]
    s = ''.join(random.choices(lst, k=20))
    print(s)

if __name__ == '__main__':
    generate()


