'''
macurl2path 模块

(功能实现模块) macurl2path 模块用于 URL 和 Macintosh 文件名的相互映射.
一般没有必要直接使用它, 请使用 urllib 中的机制.
'''
import macurl2path

file = ':my:little:pony'

print(macurl2path.pathname2url(file))
print(macurl2path.url2pathname(macurl2path.pathname2url(file)))
'''
my/little/pony
:my:little:pony
[Finished in 0.3s]
'''