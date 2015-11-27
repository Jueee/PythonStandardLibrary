'''
traceback 模块

traceback 模块允许你在程序里打印异常的跟踪返回(Traceback)信息, 类似未捕获异常时解释器所做的. 

[注]
导入 traceback 会清理掉异常状态, 所以最好别在异常处理代码中导入该模块
'''
'''
import traceback

try:
	raise(SyntaxError,'example')
except :
	traceback.print_exc()
'''


# 使用 traceback 模块将跟踪返回信息复制到字符串
# 使用 StringIO 模块将跟踪返回信息放在字符串中.
import traceback
import io

try:
	raise(IOError,'an i/o error occurred')
except:
	fp = io.StringIO()
	traceback.print_exc(file = fp)
	message = fp.getvalue()

	print('failure! the error was:', repr(message))

print('---------')



# 使用 traceback Module 模块编码 Traceback 对象
# 可以使用 extract_tb 函数格式化跟踪返回信息, 得到包含错误信息的列表
import traceback
import sys

def function():
	raise(IOError,'an i/o error occurred')

try:
	function()
except:
	info = sys.exc_info()
	for file, lineno, function, text in traceback.extract_tb(info[2]):
		print(file, 'line', lineno, 'in', function)
		print('=>', repr(text))
	print('** %s:%s' % info[:2])


