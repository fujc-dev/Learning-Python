# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 10:11
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : xiaohuar_spider.py
import re
import scrapy
from scrapy.selector import HtmlXPathSelector


class xiaohuar_spider(scrapy.Spider):
    name = "xiaohuar"  # 爬虫名称

    allowed_domains = ["xiaohuar.com"]  # 允许的域名

    start_urls = ["http://www.xiaohuar.com/hua/"]

    def parse(self, response):
        # content_url = response.url  # 当前爬取的URL
        # body = response.body  # 下载器返回的网页内容
        # unicode_body = response.body_as_unicode()  # 返回的html unicode编码
        # print content_url
        # print body
        # print unicode_body

        # hxs = HtmlXPathSelector(response)  # 创建查询对象
        # hxs = response.xpath()
        # 如果url能够匹配到需要爬取的url，即本站url
        # if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):
        # select中填写查询目标，按scrapy查询语法书写
        # items = hxs.select('//div[@class="item_list infinite_scroll"]/div')
        items = response.xpath('//div[@class="item masonry_brick"]')
        for item in items:
            src = item.xpath('.//div[@class="img"]/a/img/@src').extract()[0]
            name = item.xpath('.//div[@class="img"]/span/text()').extract()[0]
            school = item.xpath('.//div[@class="img"]/div[@class="btns"]/a/text()').extract()[0]
            print src, name, school, "\n"
