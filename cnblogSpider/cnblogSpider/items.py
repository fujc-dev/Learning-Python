# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


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

    # 对简单的Item结构化处理


'''

'''


######################################
# 下面的两个类是书上描述的ItemLoader输入输出处理器部分代码，果断没理解
# 根据书本上面的介绍：
#   好像是修改输入和输出处理，就是由于ItemLoader是用于填充Item的，
#   那么ItemLoader就包含输入和输出，既然包含输入和输出，所有会出现以
#   什么格式或者方法输入和输入内容，那么这个ItemLoader输入输出处理器的代码就用于
#   修改ItemLoader的输入输出处理器，虽然不懂MapCompose、Join是啥子意思，
#   但是大概估计就是内容格式什么的，等后续阅读再深入了解；
#   这里还包含两种输入和输出处理器设置，默认(所有属性都使用统一的处理)，再个是单个属性设置。
#   参见ProductItemLoader类
# 自定义ItemLoader，没看懂这里面有属性能做些啥子
######################################
class ProductItemLoader(ItemLoader):
    '''
        自定义ItemLoader处理
    '''
    default_output_processor = TakeFirst()
    name_in = MapCompose(unicode.title)
    name_out = Join()

    price_in = MapCompose(unicode.strip)
    # ....


######################################
# 自定义ProductItem，没看懂这里面有属性能做些啥子
# 下面这个是不在Itemloader中设置输入输出处理器时，在ProductItem中设置，
# 这个处理器有点过滤的意思
######################################
def filter_peice(value):
    if value.isdigit():  # 所有字符都是数字
        return value


class ProductItem(scrapy.Item):
    '''
        Product结构化数据模型
    '''
    name = scrapy.Field(
        # 没看懂这个
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )

    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_peice),
        output_processor=TakeFirst()
    )
