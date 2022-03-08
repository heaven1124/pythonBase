import random


def fun1():
    filename = ''
    s = 'qwertyuiopasdfghjklzxvcvbnm1234567890ASDFGHJKLPOIUYTREWQ'
    for i in range(6):
        index = random.randint(0, len(s)-1)
        filename += s[index]
    print(filename)
    return filename


def fun2():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])
        code += r
    return code


print(fun2())



