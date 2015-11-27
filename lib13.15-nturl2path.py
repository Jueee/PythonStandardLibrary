'''
nturl2path 模块

(功能实现模块) nturl2path 模块用于 URL 和 Windows 文件名的相互映射.
'''
# 使用 nturl2path 模块
import nturl2path

file = r'c:\my\little\pony'

print(nturl2path.pathname2url(file))
print(nturl2path.url2pathname(nturl2path.pathname2url(file)))





# 通过 urllib 调用 nturl2path 模块
# 2.x版本的python可以直接使用import urllib来进行操作，但是3.x版本的python使用的是import urllib.request来进行操作.
import urllib.request

file = r'c:\my\little\pony'

print(urllib.request.pathname2url(file))
print(urllib.request.url2pathname(urllib.request.pathname2url(file)))
