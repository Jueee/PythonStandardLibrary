'''
sys 模块

sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分.
'''


'''
处理命令行参数
'''
# 使用 sys 模块获得脚本的参数
# 在解释器启动后, argv 列表包含了传递给脚本的所有参数. 列表的第一个元素为脚本自身的名称.
import sys
print("script name is", sys.argv[0])
if len(sys.argv) > 1:
	print('there are', len(sys.argv)-1,'arguments')
	for arg in sys.argv[1:]:
		print(arg)
else:
	print('there are no arguments!')

'''
script name is E:\360\Python\PythonCode\01Study\03-StandardLibrary\lib01.12-sys.py
there are no arguments!
'''


'''
处理模块

path 列表是一个由目录名构成的列表, Python 从中查找扩展模块( Python 源模块, 编译模块,或者二进制扩展). 
启动 Python 时,这个列表从根据内建规则,PYTHONPATH 环境变量的内容, 以及注册表( Windows 系统)等进行初始化.
'''
'''
# 使用 sys 模块操作模块搜索路径
import sys
print('path has',len(sys.path),'members')

sys.path.insert(0,'samples')
import sample
sys.path = []
import random
'''






# 使用 sys 模块查找内建模块
# builtin_module_names 列表包含 Python 解释器中所有内建模块的名称
import sys
def dump(module):
	print(module,'=>','',end='')
	if module in sys.builtin_module_names:
		print('<BUILTIN>')
	else:
		module = __import__(module)
		print(module.__file__)

dump('os')
dump('sys')
dump('string')
# Python3 中移除了 audiodev, Bastion, bsddb185, exceptions, linuxaudiodev, md5, MimeWriter, mimify, popen2, rexec, sets, sha, stringold, strop, sunaudiodev, timing和xmllib模块 
# dump('strop')
dump('zlib')
'''
os => C:\ProgramFile\Python33\lib\os.py
sys => <BUILTIN>
string => C:\ProgramFile\Python33\lib\string.py
zlib => <BUILTIN>
'''



# 使用 sys 模块查找已导入的模块
# modules 字典包含所有加载的模块. import 语句在从磁盘导入内容之前会先检查这个字典.
import sys
print(len(sys.modules))
print(sys.modules.keys())
'''
58
dict_keys(['_weakrefset', 'os.path', 'collections.abc', 'sys', 'site', 'copyreg', 'stat', '_frozen_importlib', 'winreg', 'zipimport', 'genericpath', '_collections', 'sre_compile', 'sre_parse', 'nt', '_io', 're', 'collections', 'ntpath', '_weakref', 'errno', '_locale', 'abc', '_functools', 'string', 'encodings.cp437', '_imp', 'builtins', 'operator', 'codecs', 'encodings.gbk', 'sysconfig', 'io', 'encodings', '__main__', 'functools', 'locale', '_codecs', 'encodings.utf_8', 'heapq', 'reprlib', '_multibytecodec', 'os', '_warnings', 'itertools', 'encodings.latin_1', 'weakref', 'marshal', '_string', 'encodings.aliases', 'signal', '_sre', 'sre_constants', '_codecs_cn', 'encodings.mbcs', '_heapq', 'keyword', '_thread'])
'''



'''
处理引用记数
''' 
# 使用 sys 模块获得引用记数
# getrefcount 函数返回给定对象的引用记数 - 也就是这个对象使用次数. 
# Python 会跟踪这个值, 当它减少为 0 的时候, 就销毁这个对象.
import sys
variable = 1234
print(sys.getrefcount(0))
print(sys.getrefcount(variable))
print(sys.getrefcount(None))
# [注] 这个值总是比实际的数量大, 因为该函数本身在确定这个值的时候依赖这个对象.




# 使用 sys 模块获得当前平台
# platform 变量, 它包含主机平台的名称.
import sys
print(sys.platform)
if sys.platform == 'win32':
	import ntpath
	pathmodule = ntpath
elif sys.platform == 'mac':
	import macpath
	pathmodule = macpath
else:
	import posixpath
	pathmodule = posixpath
print(pathmodule)
'''
win32
<module 'ntpath' from 'C:\\ProgramFile\\Python33\\lib\\ntpath.py'>
'''




'''
跟踪程序
'''
# 使用 sys 模块配置分析函数
# setprofile 函数允许你配置一个分析函数(profiling function). 
# 这个函数会在每次调用某个函数或方法时被调用(明确或隐含的), 或是遇到异常的时候被调用.
import sys
def test(n):
	j = 0
	for i in range(n):
		j = j + 1
	return n
def profiler(frame,event,arg):
	print(event,frame.f_code.co_name,frame.f_lineno,'=>',arg)
# 分析函数将在下次函数调用, 返回, 或异常时激活
sys.setprofile(profiler)
# 分析这次函数调用
test(1)
# 禁用分析函数
sys.setprofile(None)
# 不会分析这次函数调用
test(2)
'''
call test 133 => None
return test 137 => 1
c_call <module> 145 => <built-in function setprofile>
'''





# 使用 sys 模块配置单步跟踪函数
# settrace 函数与此类似, 但是 trace 函数会在解释器每执行到新的一行时被调用.
import sys
def test(n):
	j = 0
	for i in range(n):
		j = j + 1
	return n
def tracer(frame,event,arg):
	print(event,frame.f_code.co_name,frame.f_lineno,'=>',arg)
	return tracer
# 分析函数将在下次函数调用, 返回, 或异常时激活
sys.settrace(tracer)
# 分析这次函数调用
test(1)
# 禁用分析函数
sys.settrace(None)
# 不会分析这次函数调用
test(2)
'''
call test 161 => None
line test 162 => None
line test 163 => None
line test 164 => None
line test 163 => None
line test 165 => None
return test 165 => 1
'''
# 基于该函数提供的跟踪功能, pdb 模块提供了完整的调试( debug )框架.





'''
处理标准输出/输入

stdin , stdout , 以及 stderr 变量包含与标准 I/O 流对应的流对象. 
如果需要更好地控制输出,而 print 不能满足你的要求, 它们就是你所需要的. 
你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们.
'''

# 使用 sys 重定向输出
# 要重定向输出只要创建一个对象, 并实现它的 write 方法.
import sys
class Redirect(object):
	"""docstring for Redirect"""
	def __init__(self, stdout):
		super(Redirect, self).__init__()
		self.stdout = stdout
	def write(self,s):
		self.stdout.write(str.lower(s))
# 重定向标准输出(包括 print 语句)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print('HEJA SVERIGE')
print('FRISKT HUMR')

# 恢复标准输出
sys.stdout = old_stdout
print('MWERWEREWVZDL!')
'''
heja sverige
friskt humr
MWERWEREWVZDL!
'''




'''
退出程序


执行至主程序的末尾时,解释器会自动退出. 
但是如果需要中途退出程序, 你可以调用 sys.exit 函数, 它带有一个可选的整数参数返回给调用它的程序.
'''
# 使用 sys 模块退出程序
'''
import sys
print('hello')
sys.exit(1)
print('world')
'''




# 捕获 sys.exit 调用
# 注意 sys.exit 并不是立即退出. 而是引发一个  SystemExit 异常. 
# 这意味着你可以在主程序中捕获对 sys.exit 的调用
import sys
print('hello')
try:
	sys.exit(1)
except SystemExit:
	print('hello world')
print('world')
'''
hello
hello world
world
'''




# 另一种捕获 sys.exit 调用的方法
# 如果准备在退出前自己清理一些东西(比如删除临时文件), 你可以配置一个 "退出处理函数"(exit handler), 它将在程序退出的时候自动被调用.
import sys
print('---------------')
def exitfunc():
	print('world')
sys.exitfunc = exitfunc
print('hello')
sys.exit(1)
print('there ')


# 在 Python 2.0 以后, 你可以使用 atexit 模块来注册多个退出处理函数.