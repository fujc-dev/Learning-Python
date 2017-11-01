
<pre>
#项目结构
     cnblogSpider
         | scrapy.cfg           项目部署文件
         | readme.md            项目描述文件
         | run.py               项目运行文件
         |-cnblogSpider         该项目的Python模块，之后可以在此加入代码
            | __init__.py
            | items.py          项目中的item文件
            | middlewares.py    项目的通信中间件
            | pipelines.py      项目中的pipelines文件
            | settings.py       项目中的配置文件
            |-spiders           方式Spider代码的目录
</pre>