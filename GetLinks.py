#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Doc description: 获取CSDN上的所有链接并去重'

__author__='HisenLee'

import urllib.request
import re

def getlink(url):
	headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0")
	# 基本的urlopen()函数不支持验证、cookie或其他HTTP高级功能。要支持这些功能，必须使用build_opener()函数来创建自己的自定义Opener对象。
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	urllib.request.install_opener(opener) #把opener安装为全局
	html = str(urllib.request.urlopen(url).read())
	# 正则解读 https? 匹配http/https  [^\s ";] 这个位置不能是空白格，也不能是引号和分号。 \.转义 \w|/ 匹配任意字母数字下划线或者/ *表示匹配前边的表达式任意次{0,}
	pattern = '(https?://[^\s)";]+\.(\w|/)*)'
	links = re.compile(pattern).findall(html)
	links = list(set(links)) # 用set把list去重
	return links

allLinks = getlink("https://blog.csdn.net/")
for link in allLinks: # 遍历输出所有链接
	print(link[0]) 
