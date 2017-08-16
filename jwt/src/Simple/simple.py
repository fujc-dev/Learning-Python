# hello.py
# -*- coding:UTF-8 -*-  //
import re

print("200 OK")
print("Content-Type: text/plain")
print("")
print("Hello CGI!")

# 求和
# _num1 = input("请输入第一个数字: ")
# _num2 = input("请输入第二个数字: ")
#
# _sum = float(_num1) + float(_num2)
# print("数字 {0} 和 {1} 相加结果为： {2}".format(_num1, _num2, _sum))

# 正则表达式

print(re.match("www", 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

print("=======================================分割线=======================================")
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")




