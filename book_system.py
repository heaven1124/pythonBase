def register():
    username = input('请输入用户名：')
    password = input('请输入密码: ')
    repasswd = input('请输入确认密码: ')

    if password == repasswd:
        # 保存用户到文件
        with open(r'D:\PycharmProjects\books\users.txt', 'a') as wsteam:
            wsteam.write('{}  {}'.format(username, password))

            print('用户注册成功！')
    else:
        print('密码不一致！')


def login():
    username = input('请输入用户名：')
    password = input('请输入密码: ')

    if username and password:
        with open(r'D:\PycharmProjects\books\users.txt', 'r') as rsteam:
            while True:
                user = rsteam.readline()  # admin  123\n
                if not user:
                    print('用户名或密码输入有误！')
                    break

                input_user = '{}  {}'.format(username, password)
                if user == input_user:
                    print('用户登陆成功！')
                    break


def show_books():
    print('---------图书馆里面的图书有：---------')
    with open(r'D:\PycharmProjects\books\books.txt', 'r', encoding='utf-8') as rsteam: # 文档里面有中文，需要转换字符编码
        books = rsteam.readlines()
        for book in books:
            print(book, end='')

show_books()



