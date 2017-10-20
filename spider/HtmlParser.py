# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 12:51
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : HtmlParser.py

import re
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, page_url, page_content):
        if page_content is None:
            return
        soup = BeautifulSoup(page_content, 'html.parser')

        _urls = set()  # 存储当前字条下所包含的其他新词条
        _datas = {}  # 当前词条爬取的数据
        # 解析内容中的新词条
        #
        """
        /item/(?:%[A-Za-z0-9]{2})+ 根据下列规则构建匹配的正则
        /item/%E4%B8%87%E7%BB%B4%E7%BD%91,
        /item/%E5%AE%B6%E5%BA%AD%E7%BD%91%E7%BB%9C,
        /item/%E4%BF%A1%E6%81%AF%E8%B5%84%E6%BA%90,
        /item/%E4%B8%87%E7%BB%B4%E7%BD%91
        """
        links = soup.findAll('a', attrs={"href": re.compile(r'/item/(?:%\w+)+')})
        for link in links:
            _urls.add(link["href"])
        # 解析词条数据
        _datas["url"] = page_url
        _title = soup.find("dd", attrs={"class": "lemmaWgt-lemmaTitle-title"}).find("h1")
        _datas["title"] = _title.getText()
        _content = soup.find('div', attrs={"class": 'lemma-summary'})
        if _content is not None:
            _datas["content"] = _content.getText()
        else:
            _datas["content"] = ""
        return _urls, _datas
