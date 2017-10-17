# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 14:28
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : Data.py

import codecs
import time


##########################
# 存储,各种存储方式
##########################
class Data(object):
    def __init__(self):
        # 构建生成的文件的文件名称
        self.filepath = "baike_%s.html" % (time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.datas = []

    ##########################
    # 检测是否包含未爬取的URL
    ##########################
    def store(self, datas):
        if datas is None:
            return
        self.datas.append(datas)

    ##########################
    # 检测是否包含未爬取的URL
    ##########################
    def output_html(self):
        fout = codecs.open(self.filepath, 'a', encoding='utf-8')
        fout.write("<HTML>")
        fout.write("<BODY>")
        fout.write("<TABLE>")
        for data in self.datas:
            fout.write("<TR>")
            fout.write("<TD STYLE=\"display:none;\">%s</TD>" % data["url"])
            fout.write("<TD>%s</TD>" % data["title"])
            fout.write("<TD>%s</TD>" % data["content"])
            fout.write("</TR>")
            self.datas.remove(data)
        fout.write("</TABLE>")
        fout.write("</BODY>")
        fout.write("</HTML>")
        fout.close()
