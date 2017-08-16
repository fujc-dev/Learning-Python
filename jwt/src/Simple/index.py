# -*- coding:UTF-8 -*-
# author:ailsabe@126.com
# //TODO 对文件功能的描述

import urllib  # 导入类库
import cmath

# 打开网址

# values = []
# values["username"] = "ailsabe@126.com"
# values["userpass"] = "123456"

# response = urllib.request.urlopen('http://www.baidu.com/')

# 读取
# html = response.read()

# 打印
# print(html)

num = float(input("请输入一个数字： "))
num_sqrt = num ** 0.5
print(num_sqrt)

num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f' % (num, num_sqrt))

num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
