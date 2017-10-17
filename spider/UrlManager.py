# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 9:33
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : UrlManager.py

###########################
# URL管理器
###########################
class UrlManager(object):
    ##########################
    # 构造函数
    # 创建两个属性，用于存储待执行的URL以及已执行的URL
    ##########################
    """ The most base type """

    def __init__(self):
        self.new_urls = set()  # 未爬取URL集合
        self.old_urls = set()  # 已爬取URL集合

    ##########################
    # 检测是否包含未爬取的URL
    ##########################
    def has_new_url(self):
        return len(self.new_urls) != 0  # 判断new_urls集合中是否函数URL
        pass

    ##########################
    # 获取一个未爬取的URL
    ##########################
    def get_new_url(self):
        _url = self.new_urls.pop()
        self.old_urls.add(_url)  # 当URL从未爬取
        return _url

    ##########################
    # 将新的URI添加到未爬取的URL集合中
    ##########################
    def add_new_url(self, url):
        if url is None:
            return
        # URL不在未爬取的URL集合中
        # 并且也不在已爬取的URL集合中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add("https://baike.baidu.com" + url)

    ##########################
    # 将新的URI添加到未爬取的URI集合中
    ##########################
    def add_new_urls(self, urls):
        # 不检测集合中的url有效性？
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    ##########################
    # 获取未爬取URL集合的大小
    ##########################
    def new_url_size(self):
        return len(self.new_urls)

    ##########################
    # 获取已爬取URL集合的大小
    ##########################
    def old_url_size(self):
        return len(self.old_urls)
