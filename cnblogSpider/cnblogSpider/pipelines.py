# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
 定制的Item Pipeline其实很简单，每个Item Pipeline组件是一个独立了的Python类，
 必须实现process_item方法，方法的原型如下：
    process_item(self, item, spider)

 每个Item Pipeline组件都需要调用process_item方法，这个方法必须返回一个item对象，或者
 抛出DropItem异常，被丢弃的Item不会被之后的Item Pipeline组件处理。
'''

import json

import pymongo
from scrapy.exceptions import DropItem


class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'wb')
        # 配置client，默认地址localhost，端口27017
        self.client = pymongo.MongoClient('localhost', 27017)

    def process_item(self, item, spider):
        '''
        :param item: 被爬取的Item
        :param spider:爬取该Item的Spider
        :return:
        '''

        if item['title']:

            # 创建一个数据库，名称store_cnblogs
            db_name = self.client['store_cnblogs']
            # 创建一个表
            cnblogs_list = db_name['cnblogs']
            cnblogs_list.insert(dict(item))
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem('这个Item被抛弃，后续不做处理')
            # Item Pipeline代码编写完毕后，需要激活才有效(setting)
