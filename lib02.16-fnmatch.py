'''
fnmatch 模块

fnmatch 模块使用模式来匹配文件名.

模式语法和 Unix shell 中所使用的相同. 
星号(*) 匹配零个或更多个字符, 问号(?) 匹配单个字符. 
你也可以使用方括号来指定字符范围, 例如 [0-9] 代表一个数字. 
其他所有字符都匹配它们本身.


glob 和 find 模块在内部使用 fnmatch 模块来实现.
'''

# 使用 fnmatch 模块匹配文件

import fnmatch
import os

for file in os.listdir('samples'):
	if fnmatch.fnmatch(file, '*.jpg'):
		print(file)




# 使用 fnmatch 模块将模式转换为正则表达式
# translate 函数可以将一个文件匹配模式转换为正则表达式.
import fnmatch
import os, re

pattern = fnmatch.translate('*.jpg')

for file in os.listdir('samples'):
	if re.match(pattern, file):
		print(file)

print('(pattern was %s)' % pattern)
