import re
import requests

# 过滤中文字符的正则表达式(中文范围) [\u4e00-\u9fa5]

msg = '古力娜扎佟丽娅迪丽热巴'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)
print(result)

result = re.match('佟丽娅', msg)  # 效果同上   match函数从头开始匹配
print(result)

result = re.search('佟丽娅', msg)  # 效果同上  search函数只匹配一次
print(result)

print(result.group())  # 提取匹配的内容

msg = 'jh3khh22213kkhgj3kl899h'
result = re.findall('[a-z][0-9]+[a-z]', msg)
print(msg)

# qq号码，5-11位，开头不能是0
qq = '843257352'
result1 = re.match('^[1-9][0-9]{4,10}$', qq)
print(result1)

# 用户名可以是字母,数字或下划线，不能以数字开头，长度必须6位以上
username = 'admin223'
result2 = re.match('^[a-zA-Z]\w{5,}$', username)
print(result2)

msg = 'aa.py ihhpyn hi.py seip.y sie.pyhi ie.txt eio.png eio.py eipyk.txt'
result3 = re.findall(r'\w*\.py\b', msg)
print(result3)

# 手机号码正则
phone = '13666666666'
result4 = re.match('1[35789]\d{9}$', phone)
print(result4)
phone1 = '010-24567829'
result41 = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone1)  # 使用()分组
print(result41.group())
print(result41.group(1))
print(result41.group(2))


# 匹配0-100数字
n = '0'
result5 = re.match(r'[1-9]?\d?$|100$', n)  # '|'表示或者
print(result5)

# 验证邮箱 163  126   QQ
email = 'uf1io@126.com'
result6 = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)  # ()和[]区别，匹配多位和匹配一位
print(result6)

# 起名的方式  （?P<名字>正则） 引用 (?P=名字)
msg = '<html><h1>abc</h1></html>'
result7 = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result7)
result8 = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>', msg)  # 使用'\number'，引用前面第number组的内容
print(result8)
print(result8.group(1))  # 分组用(),result.group()函数获取组中匹配的内容，有几个括号就有几组
print(result8.group(2))
print(result8.group(3))


# sub函数，替换
def fun(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result9 = re.sub(r'\d+', fun, 'java:56,python:68')
print(result9)

result = re.split(r'[:,]', 'java:56,python:68')
print(result)

path = '<img height="576px" src="https://m1.aboluowang.com/uploadfile/2021/1230/20211230090309249.jpg" width="1024px" loading="auto">'
result10 = re.match(r'<img height="576px" src="(.*?)"', path)
print(result10.group(1))
image_path = result10.group(1)

rep = requests.get(image_path)
with open('aa.jpg', 'wb') as wstream:
    wstream.write(rep.content)

