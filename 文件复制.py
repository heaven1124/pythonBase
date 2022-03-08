#with 结合 open使用，可以自动释放资源
import os

with open(r'd:\p1\a.jpg', 'rb') as stream: #路径前加r，保持路径里面\的原始含义，不转义
    contain = stream.read()

    file = stream.name
    filename = file[file.rfind('\\')+1:] #截取文件名
    path = os.path.dirname('__file__')  #当前文件所在的目录（绝对路径）
    path1 = os.path.join(path, filename)

    with open(path1, 'wb') as wstream:
        wstream.write(contain)
print('文件复制完成')