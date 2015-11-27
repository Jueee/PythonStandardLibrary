'''
marshal 模块

marshal 模块可以把不连续的数据组合起来 - 与字符串相互转化, 这样它们就可以写入文件或是在网络中传输.

marshal 模块使用了简单的自描述格式. 
对于每个数据项目, 格式化后的字符串都包含一个类型代码, 然后是一个或多个类型标识区域. 
整数使用小字节序( little-endian order )储存, 字符串储存时和它自身内容长度相同(可能包含空字节), 元组由组成它的对象组合表示.
'''
import marshal

value = (
    "this is a string",
    [1,2,3,4],
    ('more tuples',1.0, 2.3, 4.5),
    'this is yet another string'
	)

data = marshal.dumps(value)
# intermediate format
print(type(data), len(data))

print('-' * 50)
print(data)
print('-' * 50)

print(marshal.loads(data))







# 使用 marshal 模块处理代码
# marshal 模块还可以处理 code 对象(它用于储存预编译的 Python 模块).
import marshal

script = '''print('hello')'''

#code = complie(script, '<script>', 'exec')
data = marshal.dumps(script)

print(type(data), len(data))

print("-"*50)
print(repr(data))
print("-"*50)
exec(marshal.loads(data))