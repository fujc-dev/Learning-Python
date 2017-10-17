# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 11:47
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : HtmlDownloader.py

import requests


###########################
# HTML下载器
###########################
class HtmlDownloader(object):  # 一个普通的HTML下载类

    ###########################
    # 执行下载
    ###########################
    def download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/4.0 (compatible; MSIE5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return response.text
        return None
