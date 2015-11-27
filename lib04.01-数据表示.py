'''
数据表示

本章描述了一些用于在 Python 对象和其他数据表示类型间相互转换的模块.
这些模块通常用于读写特定的文件格式或是储存/取出 Python 变量.


4.1.1. 二进制数据

Python 提供了一些用于二进制数据解码/编码的模块. 
struct 模块用于在二进制数据结构(例如 C 中的 struct )和 Python 元组间转换. 
array 模块将二进制数据阵列 ( C arrays )封装为 Python 序列对象.


4.1.2. 自描述格式

marshal 和 pickle 模块用于在不同的 Python 程序间共享/传递数据.

marshal 模块使用了简单的自描述格式( Self-Describing Formats ), 它支持大多的内建数据类型, 包括 code 对象. 
Python 自身也使用了这个格式来储存编译后代码( .pyc 文件).
pickle 模块提供了更复杂的格式, 它支持用户定义的类, 自引用数据结构等等.
pickle 是用 Python 写的, 相对来说速度较慢, 不过还有一个 cPickle 模块, 使用 C 实现了相同的功能, 速度和 marshal 不相上下.


4.1.3. 输出格式

一些模块提供了增强的格式化输出, 用来补充内建的 repr 函数和 % 字符串格式化操作符.

pprint 模块几乎可以将任何 Python 数据结构很好地打印出来(提高可读性).
repr 模块可以用来替换内建同名函数. 该模块与内建函数不同的是它限制了很多输出形式: 他只会输出字符串的前 30 个字符, 它只打印嵌套数据结构的几个等级, 等等.


4.1.4. 编码二进制数据

Python 支持大部分常见二进制编码, 例如 base64 , binhex (一种 Macintosh格式) , quoted printable , 以及 uu 编码.


'''
