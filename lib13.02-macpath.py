'''
macpath 模块

macpath 模块( 参见 Example 13-2 )提供了 Macintosh 平台下的 os.path 功能. 
你也可以使用它在其他平台处理 Macintosh 路径.
'''
import macpath

file = 'my:little:pony'

print("isabs", "=>", macpath.isabs(file))
print("dirname", "=>", macpath.dirname(file))
print("basename", "=>", macpath.basename(file))
print("normpath", "=>", macpath.normpath(file))
print("split", "=>", macpath.split(file))
print("join", "=>", macpath.join(file, "zorba"))

'''
isabs => True
dirname => my:little
basename => pony
normpath => my:little:pony
split => ('my:little', 'pony')
join => my:little:pony:zorba
'''