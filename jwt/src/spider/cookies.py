# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 11:11
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : cookies.py

import urllib2
import cookielib


cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
reponse = urllib2.urlopen("https://www.baidu.com")

for item in cookie:
    print item.name + ":" + item.value

try:
    response = urllib2.urlopen('http://www.google.com')  # 没有达到预期的效果
    print response
except urllib2.HTTPError as e:
    if hasattr(e, 'code'):
        print 'Error Code：' + e.code
finally:
    print 'finally'
