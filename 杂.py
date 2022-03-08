# m1, m2 = input('请输入：').split(' ')
# print(m1, m2)
# a = input('请输入：书名，作者，价格（用空格分割）').split(' ')#['','','']
# print(a)
#
# isinstance(a, int)

bookname = '红楼梦'
number = 1
print('要借阅的书名是：{},借阅的数量：{}'.format(bookname, number))

#删除列表中小于50的数
def remove_from_list(list):
    n = 0
    while n < len(list):
        if list[n] < 50:
            list.remove(list[n])
        else:
            n += 1
    print(list)
