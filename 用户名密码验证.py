flag = True
while flag:
    name = input('用户名/手机号')
    if (name.islower() and name[0].isalpha() and len(name) >= 6) or (name.isdigit() and len(name) == 11):
        # 继续输入密码，输入错误允许输入多次
        while True:
            password = input('密码')
            if len(password) == 6 and password.isdigit():
                # 验证用户名，密码的正确性
                if (name == 'admin123' or name == '13999999999') and password == '123456':
                    print('登陆成功！')
                    flag = False
                    break
                else:
                    print('用户名或密码有误')
                    break
            else:
                print('密码必须是6位数字')
    else:
        print('用户名或手机号码格式错误')
