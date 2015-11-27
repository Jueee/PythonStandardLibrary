'''
uu 模块

uu 编码体系用于将任意二进制数据转换为普通文本格式. 
该格式在新闻组中很流行, 但逐渐被 base64 编码取代.

uu 编码将每个 3 字节( 24 位)的数据组转换为 4 个可打印字符(每个字符 6位), 使用从 chr(32) (空格) 到 chr(95) 的字符. 
uu 编码通常会使数据大小增加 40% .

uu 模块提供了两个函数: encode 和 decode .
'''
# 使用 uu 模块编码二进制文件
# encode(infile, outfile, filename) 函数从编码输入文件中的数据, 然后写入到输出文件中.
# infile 和 outfile 可以是文件名或文件对象.
# filename 参数作为起始域的文件名写入.
'''
import uu
import os, sys

infile = 'samples/sample.jpg'
print(type(sys.stdout),sys.stdout)
print(type(os.path.basename(infile)),os.path.basename(infile))
uu.encode(infile, sys.stdout, os.path.basename(infile))
'''





# 使用 uu 模块解码 uu 格式的文件
import uu
import io

infile = 'samples/sample.uue'
outfile = 'samples/sample.jpg'

fi = open(infile)
fo = io.StringIO()
uu.decode(fi, fo)

data = open(outfile, 'rb').read()

if fo.getvalue() == data:
	print(len(data), 'bytes ok')


