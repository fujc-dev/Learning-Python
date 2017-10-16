# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 10:59
# @Author  : ailsabe@126.com
# @Site    : IP代理使用
# @File    : IPProxy.py

import urllib2, urllib
import BeautifulSoup
import socket

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'

header = {}

header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'

request = urllib2.Request(url, headers=header)

innerHTML = urllib2.urlopen(request).read()

soup = BeautifulSoup.BeautifulSoup(innerHTML)

ips = soup.findAll('tr')  # 返回tr数组

proxyFile = open("../spider/proxy/data.txt", 'w')

for o in ips:  # 由于第一个tr行是标题，不执行解析  (1,len(ips))
    tr_classname = o.get("class")
    if tr_classname is None: continue
    tds = o.findAll("td")
    proxyFile.write(tds[1].string + "\t" + tds[2].string + "\n")
proxyFile.close()
# 检测代理是否可用

socket.setdefaulttimeout(3)

proxyFile = open('../spider/proxy/data.txt', 'r')
lines = proxyFile.readlines()
proxys = []
for line in lines:
    ip = line.strip("\n").split("\t")
    proxy_host = "http://" + ip[0] + ":" + ip[1]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)
    url = "http://ip.chinaz.com/getip.aspx"

# a).ip = lines[i].strip("\n").split("\t") 这个是去掉每行末尾的换行符（也就是"\n"）,
# 然后以制表符（也就是"\t"）分割字符串为字符串数组

# b).proxy_temp = {"http":proxy_host}其中http代表代理的类型，
# 除了http之外还有https，socket等这里就以http为例

# c).urllib.urlopen(url,proxies=proxy) 其中proxies就是代理。
# 以代理模式访问目标网址

# d).socket.setdefaulttimeout(3)设置全局超时时间为3s，也就是说，
# 如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）

for proxy in proxys:
    try:
        res = urllib.urlopen(url, proxies=proxy).read()
        print res
    except Exception, e:
        print proxy
        print e
        continue
