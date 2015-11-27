'''
ntpath 模块

ntpath 模块( 参见 Example 13-3 )提供了 Windows 平台下的 os.path 功能.
你也可以使用它在其他平台处理 Windows 路径.
'''
import ntpath

file = "/my/little/pony"

print("isabs", "=>", ntpath.isabs(file))
print("dirname", "=>", ntpath.dirname(file))
print("basename", "=>", ntpath.basename(file))
print("normpath", "=>", ntpath.normpath(file))
print("split", "=>", ntpath.split(file))
print("join", "=>", ntpath.join(file, "zorba"))

'''
isabs => True
dirname => /my/little
basename => pony
normpath => \my\little\pony
split => ('/my/little', 'pony')
join => /my/little/pony\zorba
'''




