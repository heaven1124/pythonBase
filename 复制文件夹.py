import os.path


def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        #获取源文件夹里面的文件
        filelist = os.listdir(src)
        # 遍历所有文件
        for file in filelist:
            # 拼接文件路径
            path = os.path.join(src, file)
            # 判断是文件夹还是文件
            if os.path.isdir(path):
                # 递归调用copy
                # os.mkdir(target/path)目标文件夹中递归创建文件夹？
                copy(path, target)
            else:
                # 不是文件夹直接进行复制
                with open(path, 'rb') as rstream:
                    container = rstream.read()
                    path1 = os.path.join(target, file)
                    with open(path1, 'wb') as wstream:
                        wstream.write(container)
        else:
            print('复制完毕！')
