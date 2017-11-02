# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector
from scrapy import FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request


class ZhihuComSpider(CrawlSpider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/tombkeeper']

    # rules = (
    #     Rule(LinkExtractor(allow=r'people/'), callback='parse_item', follow=True),
    # )


    # 替换原来的start_requests，callback为
    def start_requests(self):
        return [Request("http://www.zhihu.com/#signin", meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        print 'Preparing login'
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = response.xpath('.//input[@name="_xsrf"]/@value').extract()
        # 为什么这种Selector的方式会报异常，暂时没有研究
        # Selector(response.text).xpath('.//input[@name="_xsrf"]/@value').extract()
        print xsrf[0]
        pass
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数
        # return [FormRequest.from_response(response,  # "http://www.zhihu.com/login",
        #                                   meta={'cookiejar': response.meta['cookiejar']},
        #                                   headers=self.headers,
        #                                   formdata={
        #                                       '_xsrf': xsrf,
        #                                       'email': '1527927373@qq.com',
        #                                       'password': '321324jia'
        #                                   },
        #                                   callback=self.after_login,
        #                                   dont_filter=True
        #                                   )]

    # make_requests_from_url会调用parse，就可以与CrawlSpider的parse进行衔接了
    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
