'''
mimetypes 模块

mimetypes 模块可以判断给定 url ( uniform resource locator , 统一资源定位符) 的 MIME 类型. 

它基于一个内建的表, 还可能搜索 Apache 和 Netscape的配置文件.

'''

import mimetypes
import glob
from urllib import __path__

print(dir(__path__))
for file in glob.glob('samples/*'):
	url = parse.parse(file)
	print(file, mimetypes.guess_type(url))