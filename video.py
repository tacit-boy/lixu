#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: lee_xu@foxmail.com
# date: 2017-09-11
# 作用: 抓取网页链接并输出表格

import urllib2
import re

# 获取网页内容
data = urllib2.urlopen('http://www.dytt8.net/html/dongman/hy/20120503/37536.html').read()

# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
    print url.decode('gb2312')
