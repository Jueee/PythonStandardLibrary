'''
imp 模块

imp 模块包含的函数可以用于实现自定义的 import 行为.
'''
import imp
import sys

def my_import(name, globals = None, locals = None, fromlist = None):
	try:
		module = sys.modules[name]
	except KeyError:
		file, pathname, description = imp.find_module(name)
		print('import', name, 'from', pathname, description)
		module = imp.load_module(name, file, pathname, description)
	return module

my_import('sys')



