'''
mmap 模块

mmap 模块提供了操作系统内存映射函数的接口. 
映射区域的行为和字符串对象类似, 但数据是直接从文件读取的.
'''
# 使用 mmap 模块
import mmap
import os

filename = 'samples/sample.txt'

# 在 Windows 下, 这个文件必须以既可读又可写的模式打开( `r+` , `w+` , 或`a+` ), 否则 mmap 调用会失败.
file = open(filename, 'r+')
size = os.path.getsize(filename)

data = mmap.mmap(file.fileno(), size)

# basics
print(data)
print(len(data), size)

# 使用切片操作读取文件
print(repr(data[:10]), repr(data[:10]))

# 或使用标准的文件接口
print(repr(data.read(10)), repr(data.read(10)))




# 对映射区域使用字符串方法和正则表达式
# 内存映射区域的使用:
# 在很多地方它都可以替换普通字符串使用, 包括正则表达式和其他字符串操作.
import mmap
import os,re

def mapfile(filename):
	file = open(filename, 'r+')
	size = os.path.getsize(filename)
	return mmap.mmap(file.fileno(), size)

data = mapfile('samples/sample.txt')
print(data)

# search
index = data.find(b'small')
print(index, repr(data[index-5:index+15]))

# regualr expressions work too !
print(data.read().decode())
m = re.search('samll', data.read().decode())
if m:
	print(m.start(),m.group(1))









