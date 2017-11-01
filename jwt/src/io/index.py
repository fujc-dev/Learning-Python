# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/1 17:57
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : index.py

import os

try:
    import cPickle as pickle
except ImportError:
    import pickle

# IO编程
# 打开文件
# 由于文件操作可能会出现IO异常，一旦出现IO异常，后面的close()方法就不会调用
# 所以为了保证程序的健壮性，我们需要使用try...finally来实现。

# 方式1
# try:
#     _data = open(r'D:\Github\Learning-Python\files\data.txt')
#     print _data.read()
# finally:
#     _data.close()

# 方式2
with open(r'D:\Github\Learning-Python\files\data.txt', 'r', 2) as fileReader:
    for line in fileReader.readlines():
        print line.strip()

# 文件写入
_ = open(r'D:\Github\Learning-Python\files\data.txt', 'w')
_.write("学习之旅")
_.close()

with open(r'D:\Github\Learning-Python\files\data.txt', 'w') as fileWriter:
    fileWriter.write("Python 学习之旅")

# 文件操作和目录


# 获取当前脚本工作的目录路劲
print os.getcwd()
# 获取指定文件夹下的所有文件和文件夹目录
print os.listdir("D:\Github")
# 检测文件是否存在
_isfile = os.path.isfile("D:\Github\Learning-Python\\files\\remove.txt")
print _isfile
# 删除一个文件
if _isfile:
    os.remove("D:\Github\Learning-Python\\files\\remove.txt")
# 检测文件夹是否有效
print os.path.isdir("D:\Github\Learning-Python\\files\\aa")

print os.path.isabs("D:\Github\Learning-Python\\files\data.txt")

# 序列化与反序列化
d = dict(url="index.html", title="首页", content="首页")
fileW = open(r'D:\Github\Learning-Python\\files\data.txt', 'wb')
print pickle.dump(d, fileW)
fileW.close()

fileR = open(r'D:\Github\Learning-Python\\files\data.txt','rb')
d = pickle.load(fileR)
fileR.close()
print d

