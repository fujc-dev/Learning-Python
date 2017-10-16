# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 15:08
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : seputu.py

import requests
import BeautifulSoup

user_agent = "Mozilla/4.0 (comatible; MSTE 5.5;Windows NT)"

headers = {"User-Agent": user_agent}

r = requests.get("http://seputu.com/", headers=headers)

# print r.content

soup = BeautifulSoup.BeautifulSoup(r.content, fromEncoding='utf-8')

for mulu in soup.findAll(attrs={"class": "mulu"}):  # 从当前文档中查询所有的class值为mulu的标签
    h2 = mulu.find('h2')  # 检测是否包含标题
    if h2 is not None:  # 标题为空不做处理
        h2_title = h2.string
        for a in mulu.find(attrs={"class": "box"}).findAll("a"):
            href = a.get('href')  # 获取文本内容
            title = a.get('title') # 获取标题
            print href, title

# 将抓取的内容存储到MySql
