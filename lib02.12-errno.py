'''
errno 模块

errno 模块定义了许多的符号错误码, 比如 ENOENT ("没有该目录入口") 以及EPERM ("权限被拒绝"). 
它还提供了一个映射到对应平台数字错误代码的字典.

在大多情况下,  IOError 异常会提供一个二元元组, 包含对应数值错误代码和一个说明字符串. 
如果你需要区分不同的错误代码, 那么最好在可能的地方使用符号名称.
'''
import errno

try:
	fp = open('no.such.file')
except IOError as error:
	print(error.args[0])
	error = error.args[0]
	if error == errno.ENOENT:
		print('no such file')
	elif error == errno.EPERM:
		print('permission denied')
	else:
		print('message')



print('---------')




# 使用 errorcode 字典
# 如何使用 errorcode 字典把数字错误码映射到符号名称( symbolic name ).
import errno

try:
	fp = open('no.such.file')
except IOError as e:
	error = e.args[0]
	message = e.args[1]
	print(error,repr(message))
	print(errno.errorcode[error])