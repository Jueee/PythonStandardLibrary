'''
getopt 模块

getopt 模块包含用于抽出命令行选项和参数的函数, 它可以处理多种格式的选项.

其中第 2 个参数指定了允许的可缩写的选项. 
选项名后的冒号(:) 意味这这个选项必须有额外的参数.
'''
# 使用 getopt 模块
import getopt
import sys

# 模仿命令行参数
sys.argv = ['myscript.py','-1','-d','directory','filename']

# 处理选项
opts,args = getopt.getopt(sys.argv[1:], '1d:')
print('opts','=>',opts)
print('args','=>',args)

long = 0
directory = None

for o,v in opts:
	if o ==  '-1':
		long = 1
	elif o == '-d':
		directory = v

print('long','=',long)
print('directory','=',directory)
print('arguments','=',args)
'''
opts => [('-1', ''), ('-d', 'directory')]
args => ['filename']
long = 1
directory = directory
arguments = ['filename']
'''
print('------------')



# 使用 getopt 模块处理长选项
# 为了让 getopt 查找长的选项, 如 Example 2-24 所示, 传递一个描述选项的列表做为第 3 个参数.
# 如果一个选项名称以等号(=) 结尾, 那么它必须有一个附加参数.
import getopt
import sys

# 模仿命令行参数
sys.argv = ['myscript.py', '--echo', '--printer', '1p01', 'message']

opts, args = getopt.getopt(sys.argv[1:], 'ep:', ['echo', 'printer='])
print('opts','=>',opts)
print('args','=>',args)

# 处理选项
echo = 0
printer = None

for o,v in opts:
	if o in ('-e','--echo'):
		echo = 1
	elif o in ('-p','--printer'):
		printer = v

print('long','=',long)
print('directory','=',directory)
print('arguments','=',args)

'''
opts => [('--echo', ''), ('--printer', '1p01')]
args => ['message']
long = 1
directory = directory
arguments = ['message']
'''

