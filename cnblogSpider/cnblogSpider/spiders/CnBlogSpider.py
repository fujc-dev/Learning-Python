# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 16:54
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : CnBlogSpider.py

import scrapy
import re
from scrapy import Selector

from cnblogSpider.items import CnblogSpiderItem

'''
    1、爬虫文件需要定义一个类，并继承scrapy.Spider
    2、必须定义name即爬虫名，如果没有name，会报错。
    3、编写函数parse，这里需要注意的是，该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse；
    4、定义需要爬取的url，放在列表中，因为可以爬取多个url，Scrapy源码是一个For循环，从上到下爬取这些url，使用生成器迭代将url发送给下载器下载url的html
'''


class CnBlogsSpider(scrapy.Spider):
    #
    name = 'cnblogs'  # 爬虫的名称
    #
    allowed_domains = ['cnblogs.com']  # 允许的域名
    #
    start_urls = [
        'https://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]


    ###############################
    # 重写parse回调函数
    ###############################
    def parse(self, response):
        # print response.url
        # 实现网页解析代码
        # 首先抽取所有的文章
        papers = response.xpath('.//*[@class="day"]')
        # 从每篇文章中抽取数据
        for paper in papers:
            url = paper.xpath('.//*[@class="postTitle"]/a/@href').extract()[0]
            title = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
            time = paper.xpath('.//*[@class="dayTitle"]/a/text()').extract()[0]
            content = paper.xpath('.//*[@class="c_b_p_desc"]/text()').extract()[0]
            # 根据定义的Item创建结构化的数据
            item = CnblogSpiderItem(url=url, title=title, time=time, content=content)
            # print url, title, time, content
            yield item  # 代码最后使用yield关键字提交item，将parse方法打造成一个生成器(搞不懂，死记硬背吧)
        #############################################
        # 为了实现数据的持续性抓取，页面中需要处理有效的子URL，翻页等
        # 目前这个调度器里面只有一个有效的URL可以被抓取
        # 实现翻页处理
        # 实现翻页本质上是构建一个Request并提交给Scrapy引擎的过程
        #############################################
        next_page_selector = Selector(response).re(u'<a href="(?:\S*page=[0-9]*)">下一页</a>')
        if next_page_selector:
            next_page = re.findall(u'(?:http://www.cnblogs.com/qiyeboy/default.html\?page=[0-9]*)',
                                   next_page_selector[0])
            if next_page:
                print next_page[0]
                yield scrapy.Request(url=next_page[0], callback=self.parse)

# if __name__ == '__main__':
#     pass
