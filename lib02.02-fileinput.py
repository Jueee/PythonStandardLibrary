'''
fileinput 模块

fileinput 模块允许你循环一个或多个文本文件的内容
'''


# 使用 fileinput 模块循环一个文本文件
import fileinput
import sys

for line in fileinput.input('samples/sample.txt'):
	sys.stdout.write('=>')
	sys.stdout.write(line)



# 使用 fileinput 模块处理多个文本文件  
# 也可以使用 fileinput 模块获得当前行的元信息 (meta information). 
# 其中包括 isfirstline(判断是否文件开始) , filename(文件名称) , lineno(行号)
import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('samples/*.txt')):
	if fileinput.isfirstline(): # first in a file?
		sys.stderr.write('--reading %s --\n' % fileinput.filename())
	sys.stdout.write(str(fileinput.lineno()) + ' -> ' + str.upper(line))





# 使用 fileinput 模块将 CRLF 改为 LF
# CRLF -- Carriage-Return Line-Feed 回车换行
# LF   -- ASCII代码控制字符，对应的字符是换行符，Line Feed，ASCII值是10。
# 文本文件的替换操作，只需要把 inplace 关键字参数设置为 1 , 传递给 input 函数, 该模块会帮你做好一切.
import fileinput,sys

for line in fileinput.input(inplace = 1):
	if line[-2:] == '\r\n':
		line = line[:2] + '\n'
	sys.stdout.write(line)






