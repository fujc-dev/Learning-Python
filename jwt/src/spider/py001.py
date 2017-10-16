# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 9:06
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : py001.py

import urllib
import BeautifulSoup
import MySQLdb


class DBHelper(object):
    def __init__(self, host="127.0.0.1", user="root", passwd="ailsabe@126.com", db="TESTDB"):
        # 当connection不为null时，关闭连接
        # if not self.connection is None: self.connection.close()
        self.connection = MySQLdb.connect(host=host,
                                          user=user,
                                          passwd=passwd,
                                          db=db,
                                          port=3306,
                                          charset="utf8")
        self.cursor = self.connection.cursor()

    def execute(self, query, args=None):
        self.cursor.execute(query, args)
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()


# 创建请求
request = urllib.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
#
# print request.read()
################################################
soup = BeautifulSoup.BeautifulSoup(request)
################################################
# 使用库BeautifulSoup获取id为book的div标签
_bookDiv = soup.find(attrs={"id": "book"})
# 通过class="title"获取所有的book  a标签
_bookA = _bookDiv.findAll(attrs={"class": "title"})
# 是遍历book_a所有的a标签
db = DBHelper()
# 创建一个存储抓去的网页数据的表，ID，地址，名称

# DROP TABLE IF EXISTES Book

db.execute('DROP TABLE IF EXISTS Book')

createBoolSQL = 'CREATE TABLE Book (ID INT(20) NOT NULL AUTO_INCREMENT,Name VARCHAR(50) NOT NULL,HREF VARCHAR(200) NOT NULL,PRIMARY KEY(ID) )'

db.execute(createBoolSQL)

data = db.execute('SELECT VERSION()')

print "Database version : %s " % data
for book in _bookA:
    name = book.string
    href = book.get('href')
    insertSQL = "INSERT INTO BOOK(NAME,HREF)VALUES('" + name + "','" + href + "')"
    db.execute(insertSQL)
db.commit()
db.close()
# 是输出a标签中的内容


# 将抓取的数据存储到Mysql数据库()

#






# connection.close()
