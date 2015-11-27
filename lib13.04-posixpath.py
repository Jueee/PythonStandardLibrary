'''
posixpath 模块

posixpath 模块提供了 Unix 和其他 POSIX 兼容平台下的 os.path 功能. 
你也可以使用它在其他平台处理 POSIX 路径. 
另外, 它也可以处理 URL .
'''

import posixpath

file = "/my/little/pony"
print("isabs", "=>", posixpath.isabs(file))
print("dirname", "=>", posixpath.dirname(file))
print("basename", "=>", posixpath.basename(file))
print("normpath", "=>", posixpath.normpath(file))
print("split", "=>", posixpath.split(file))
print("join", "=>", posixpath.join(file, "zorba"))
'''
isabs => True
dirname => /my/little
basename => pony
normpath => /my/little/pony
split => ('/my/little', 'pony')
join => /my/little/pony/zorba
'''