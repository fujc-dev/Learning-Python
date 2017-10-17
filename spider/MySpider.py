# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 14:22
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : MySpider.py

from UrlManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from Data import Data


class MySpider(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = Data()

    def start(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                old_url = self.manager.get_new_url()
                inner_html = self.downloader.download(old_url)
                _urls, _datas = self.parser.parser(old_url, inner_html)
                # 存储
                self.manager.add_new_urls(_urls)
                self.output.store(_datas)
            except Exception, e:
                print 'start failed'
        self.output.output_html()
