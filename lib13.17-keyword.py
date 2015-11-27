'''
keyword 模块

keyword 模块有一个包含当前 Python 版本所使用的关键字的列表.

它还提供了一个字典, 以关键字作为 key , 以一个描述性函数作为 value , 它可用于检查给定单词是否是 Python 关键字.
'''
import keyword

name = input('Enter module name:')

if keyword.iskeyword(name):
	print(name,'is a reserved word.')
	print("here's a complete list of reserved words")
	print(keyword.kwlist)