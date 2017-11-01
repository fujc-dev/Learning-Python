# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 9:33
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : URLManager.py

import cPickle
import hashlib


###########################
# URL管理器,简单从分布式的URI管理器需要做一些优化，
# 1、依然才去set内存去冲方式
# 2、由于直接存储URL大量的URL，尤其是URL链接很长时，很容易造成内容溢出，所以
#    我们将爬取的进行MD5处理。
###########################
class URLManager(object):
    ##########################
    # 构造函数
    # 创建两个属性，用于存储待执行的URL以及已执行的URL
    ##########################
    """ The most base type """

    def __init__(self):
        self.new_urls = self.load_progress("new_urls")  # 未爬取URL集合
        self.old_urls = self.load_progress("old_urls")  # 已爬取URL集合

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
        md5 = hashlib.md5()
        md5.update(_url)
        self.old_urls.add(md5.hexdigest()[8:-8])  # 当URL从未爬取
        return _url

    ##########################
    # 将新的URI添加到未爬取的URL集合中
    ##########################
    def add_new_url(self, url):
        if url is None:
            return
        # URL不在未爬取的URL集合中
        # 并且也不在已爬取的URL集合中
        md5 = hashlib.md5()
        url_md5 = md5.update(url)
        if url not in self.new_urls and url_md5 not in self.old_urls:
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

    ##########################
    # 从文件中加载进度
    ##########################
    def load_progress(self, path):
        print '[+]从文件加载进度：%s' % path
        try:
            with open(path, 'rb') as f:
                tmp = cPickle.load(f)
                return tmp
        except:
            print '[!]无进度文件，创建：%s' % path
        return set()

    ##########################
    # 保存进度
    ##########################
    def save_progress(self, path, data):
        with open(path, 'rb') as f:
            cPickle.dump(data, f)
