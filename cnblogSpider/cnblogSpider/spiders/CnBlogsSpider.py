# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 16:54
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : CnBlogsSpider.py

import scrapy


class CnBlogsSpider(scrapy.Spider):
    name = 'cnblogs'  # 爬虫的名称
    allowed_domains = ['www.cnblogs.com']  # 允许的域名
    start_urls = [
        'https://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]

    def parse(self, response):
        # 实现网页解析代码
        pass
