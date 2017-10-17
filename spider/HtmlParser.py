# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 12:51
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : HtmlParser.py

import re
import BeautifulSoup


class HtmlParser(object):
    def parser(self, page_url, page_content):
        if page_content is None:
            return
        soup = BeautifulSoup.BeautifulSoup(page_content, fromEncoding='UTF-8')

        _urls = set()  # 存储当前字条下所包含的其他新词条
        _datas = {}  # 当前词条爬取的数据
        # 解析内容中的新词条
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
        return _urls, _datas
