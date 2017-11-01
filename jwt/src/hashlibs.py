# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 13:36
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : hashlibs.py


import hashlib

# ######## md5 ########

string = "beyongjie"

md5 = hashlib.md5()
md5.update(string.encode('utf-8'))  # 注意转码
res = md5.hexdigest()
print("md5加密结果:", res)

# ######## sha1 ########

sha1 = hashlib.sha1()
sha1.update(string.encode('utf-8'))
res = sha1.hexdigest()
print("sha1加密结果:", res)

# ######## sha256 ########

sha256 = hashlib.sha256()
sha256.update(string.encode('utf-8'))
res = sha256.hexdigest()
print("sha256加密结果:", res)

# ######## sha384 ########

sha384 = hashlib.sha384()
sha384.update(string.encode('utf-8'))
res = sha384.hexdigest()
print("sha384加密结果:", res)

# ######## sha512 ########

sha512 = hashlib.sha512()
sha512.update(string.encode('utf-8'))
res = sha512.hexdigest()
print("sha512加密结果:", res)
