# 把本来不是可迭代对象变成可迭代对象
import hashlib


def main():
    digester = hashlib.md5()
    with open('aa.docx', 'rb') as file_stream:
        file_iter = iter(lambda: file_stream.read(1024), b'')
        for data in file_iter:
            digester.update(data)
    print(digester.hexdigest())

redis
if __name__ == '__main__':
    main()