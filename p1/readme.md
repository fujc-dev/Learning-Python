
项目结构
     cnblogSpider
         | scrapy.cfg           项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中）
         |
         |-cnblogSpider         该项目的Python模块，之后可以在此加入代码
            | __init__.py
            | items.py          设置数据存储模板，用于结构化数据，如：Django的Model
            | middlewares.py
            | pipelines.py      数据处理行为，如：一般结构化的数据持久化
            | settings.py       配置文件，如：递归的层数、并发数，延迟下载等
            |-spiders           爬虫目录，如：创建文件，编写爬虫规则