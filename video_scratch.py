#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: lee_xu@foxmail.com
# date: 2017-09-11
# 作用: 抓取剧集网页链接并输出
# 用法：python video_scratch.py <link>
# 例子：python video_scratch.py http://www.dytt8.net/html/tv/oumeitv/20170603/54148.html

import re
import sys
import urllib2

html = urllib2.urlopen('%s' % sys.argv[1]).read()
links = re.findall('"((ftp)s?://.*?)"', html)
for url in links:
    print url[0].decode('gb2312')
