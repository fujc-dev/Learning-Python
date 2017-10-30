# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 15:15
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : CnBlogSpiderItem.py

import scrapy


class CnBlogSpiderItemItem(scrapy.Item):
    # 定义项的字段
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    pass


# if __name__ == '__main__':
#     item = CnBlogSpiderItemItem(title='Python爬虫', content="爬虫开发")
#     print item["title"]
