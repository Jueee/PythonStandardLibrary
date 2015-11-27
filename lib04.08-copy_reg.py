'''
copy_reg 模块

可以使用 copy_reg 模块注册你自己的扩展类型. 
这样 pickle 和 copy 模块就会知道如何处理非标准类型.



Python 2								  Python 3
①	
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO                       import io
②	
try:
    import cPickle as pickle
except ImportError:
    import pickle                         import pickle
③	import __builtin__	                  import builtins
④	import copy_reg	                      import copyreg
⑤	import Queue	                      import queue
⑥	import SocketServer	                  import socketserver
⑦	import ConfigParser	                  import configparser
⑧	import repr	                          import reprlib
⑨	import commands	                      import subprocess
'''
import pickle

CODE = '''print('good evening')'''

exec(CODE)
exec(pickle.loads(pickle.dumps(CODE)))








# 使用 copy_reg 模块实现 code 对象的 pickle 操作
# 可以注册一个 code 对象处理器来完成目标. 
# 处理器应包含两个部分: 
# 一个 pickler , 接受 code 对象并返回一个只包含简单数据类型的元组, 以及一个 unpickler , 作用相反, 接受这样的元组作为参数.
import copyreg
import pickle, marshal, types

# register a pickle handler for code objects

def code_unpickler(data):
	return marshal.loads(data)

def code_pickler(copy):
	return code_unpickler,(marshal.dumps(code),)

copyreg.pickle(types.CodeType, code_pickler, code_unpickler)

# try it out
CODE = """
print("suppose he's got a pointed stick")
"""
# code = compile(CODE, "<string>", "exec")
code = CODE
exec(code)
exec(pickle.loads(pickle.dumps(code)))
'''
如果你是在网络中传输 pickle 后的数据, 那么请确保自定义的 unpickler 在数据接收端也是可用的.
'''






# 使用 copy_reg 模块实现文件对象的 pickle 操作
# 实现 pickle 一个打开的文件对象.
import copyreg
import pickle, types
import io

def file_unpickler(position, data):
	file = io.StringIO(data)
	file.seek(position)
	return file

def file_pickler():
	position = file.tell()
	file.seek(0)
	data = file.read()
	file.seek(position)
	return file_unpickler,(position, data)

#copyreg.pickle(types.FileType, file_pickler, file_unpickler)

file = open("samples/sample.txt", "rb")
print(file.read(120),)
print("<here>",)
print(pickle.loads(pickle.dumps(file)).read())





