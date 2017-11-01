# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


######################################
# 定义Item
# 爬取的主要目标就是从非结构的数据源提取出结构性的数据
######################################
class CnblogSpiderItem(scrapy.Item):
    # 定义项的字段
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
