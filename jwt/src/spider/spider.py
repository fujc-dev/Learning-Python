# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 9:11
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : spider.py


import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
from lxml import etree

# # 使用urllib2实现一个完整的请求与响应模型
# response = urllib2.urlopen("http://www.zhihu.com")
# innerHTML = response.read()
# print innerHTML
#
# # 请求
# requet = urllib2.Request("http://www.zhihu.com")
# # 响应
# response = urllib2.urlopen(requet)
# innerHTML = response.read()
# print innerHTML

# # POST请求演示
# postdata = {'username': 'zhangsan', 'password': '123456'}
# data = urllib.urlencode(postdata)
# requet = urllib2.Request('http://www.simple.com/login')
# response = urllib2.urlopen(requet)
# innerHTML = response.read()
# print innerHTML

# # 请求头Header处理
# url = 'http://www.simple.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSTE 5.5; Windows NT)'  # 用于包含请求的用户信息，其中有使用浏览器的型号、版本和操作系统信息，这个头域经常用来做完反爬虫的措施
# referer = 'http://www.simple.com'
# postdata = {'username': 'zhangsan', 'password': '123456'}
# # 将user_agent,referer写入头信息
# headers = {'User-Agent': user_agent, 'Referer': referer}
# data = urllib.urlencode(postdata)
#
# # 设置请求Header方式1
# request = urllib2.Request(url, data=data, headers=headers)
# # 设置请求Header方式2
# request = urllib2.Request(url)
# request.add_header('User-Agent', user_agent)
# request.add_header('eferer', referer)
# response = urllib2.urlopen(request)
#
# innerHTML = response.read()

htmlText = '''
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no, width=device-width">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="format-detection" content="telephone=no" />
  <title>重庆OA系统</title>
  <link rel="manifest" href="manifest.json">
  <!-- un-comment this code to enable service worker
  <script>
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('service-worker.js')
        .then(() => console.log('service worker installed'))
        .catch(err => console.log('Error', err));
    }
  </script>-->
  <!-- jQuery Include -->
  <!--<script src="lib/jquery/jquery.min.js"></script>-->
  <!-- Bootstrap Include -->
  <!--<link rel="stylesheet" type="text/css" href="http://www.jq22.com/jquery/bootstrap-3.3.4.css">-->
  <link href="lib/ionic/css/ionic.css" rel="stylesheet">
  <link href="css/style.css" rel="stylesheet">
  <link href="css/receive.css" rel="stylesheet">
  <link href="lib/datepicker-for-ionic/dist/style.css" rel="stylesheet">
  <!--<link href="css/pdf/tooltipster.min.css" rel="stylesheet">-->
  <!-- IF using Sass (run gulp sass first), then uncomment below and remove the CSS includes above
  <link href="css/ionic.app.css" rel="stylesheet">
  -->
  <!-- ionic/angularjs js -->
  <script src="lib/ionic/js/ionic.bundle.js"></script>
  <script src="lib/ngCordova/dist/ng-cordova.min.js"></script>
  <script src="lib/datepicker-for-ionic/dist/templates.min.js"></script>
  <script src="lib/datepicker-for-ionic/dist/ionic-datepicker.min.js"></script>
  <!-- cordova script (this will be a 404 during development) -->
  <script src="cordova.js"></script>
  <!-- my app's js -->
  <script src="js/app.js"></script>
  <script src="js/controllers.js"></script>
  <script src="js/services.js"></script>
  <script src="js/directives.js"></script>
  <script src="js/public.js"></script>
  <script src="js/jquery-3.1.1.min.js"></script>
  <script src="js/errorTip.js"></script>

  <script src="js/core/Core.js"></script>
  <script src="js/core/DispatchService.js"></script>
  <script src="js/core/UtilService.js"></script>

  <!-- 待办事宜 -->
  <script src="js/services/receiveService.js"></script>
  <script src="js/controllers/receiveCtrl.js"></script>
  <script src="js/controllers/dispatchCtrl.js"></script>
  <script src="js/controllers/informCtrl.js"></script>
  <script src="js/controllers/reportCtrl.js"></script>
  <!-- 个人收藏 -->
  <script src="js/controllers/collectionCtrl.js"></script>
  <script src="js/services/collectionService.js"></script>
  <!-- 在办事宜 -->
  <script src="js/controllers/doingCtrl.js"></script>
  <!-- 历史公文 -->
  <script src="js/controllers/historyCtrl.js"></script>

  <!-- Mobiscroll JS and CSS Includes -->
  <link href="lib/mobiscroll/mobiscroll-2.13.2.full.min.css" rel="stylesheet" type="text/css"/>
  <script src="lib/mobiscroll/mobiscroll-2.13.2.full.min.js" type="text/javascript"></script>

</head>
<body ng-app="starter">
<!--
  The nav bar that will be updated as we navigate between views.
-->
<ion-nav-bar class="bar-positive">
  <ion-nav-back-button>
  </ion-nav-back-button>
</ion-nav-bar>
<!--
  The views will be rendered in the <ion-nav-view> directive below
  Templates are in the /templates folder (but you could also
  have templates inline in this html file if you'd like).
-->
<ion-nav-view></ion-nav-view>
</body>
</html>
'''
soup = BeautifulSoup(htmlText, 'lxml', from_encoding='utf-8')
print soup.title
for meta in soup.meta.contents:
    print meta
print soup.title.string
