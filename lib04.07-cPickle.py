'''
cPickle 模块

cPickle 模块是针对 pickle 模块的一个更快的实现
'''
try:
	import cPickle
	pickle = cPickle
except ImportError:
	import pickle
	