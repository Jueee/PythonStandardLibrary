'''
urlparse 模块

urlparse 模块包含用于处理 URL 的函数, 可以在 URL 和平台特定的文件名间相互转换.
'''
# 使用 urlparse 模块
from urllib.parse import urlparse

print(dir(urlparse))
print(urlparse('http://www.baidu.com?ca=123#12313'))





# 使用 urlparse 模块处理 HTTP 定位器( HTTP Locators )
import urllib.parse

scheme, host, path, params, query, fragment = urllib.parse.urlparse('http://www.baidu.com?ca=123#12313')

if scheme == 'http':
	print('host', '=>', host)
	if params:
		path = path + ';' + params
	if query:
		path = path + '?' + query
	print('path', '=>', path)

print('----------------------')

# 使用 urlparse 模块处理 HTTP 定位器( HTTP Locators )
import urllib.parse

scheme, host, path, params, query, fragment = urllib.parse.urlparse('http://host/path;params?query#fragment')
print(dir(urllib.parse))
if scheme == 'http':
	print('host', '=>', host)
	print('path', '=>', urllib.parse.urlunparse(('', '', path, params, query, '')))






# 使用 urlparse 模块组合相对定位器
# 使用 urljoin 函数将绝对路径和相对路径组合起来.
import urllib.parse

base = 'http://spam.egg/my/little/pony'

for path in  '/index', 'goldfish', '../black/cat':
	print(path, '=>', urllib.parse.urljoin(base, path))