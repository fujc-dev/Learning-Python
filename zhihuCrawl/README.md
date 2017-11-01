<pre>
    实战项目：Scrapy爬虫

    主题：爬取知乎网站上用户的信息以及人际关系等

    # 创建Scrapy项目
    scrapy startpeoject zhihuCrawl

    # 通过genspider命令创建基于CrawlSpider的爬虫模版
    scrapy genspider -t crawl zhihu.com zhihu.com
</pre>