'''
atexit 模块

atexit 模块允许你注册一个或多个终止函数(暂且这么叫), 这些函数将在解释器终止前被自动调用.
'''

# 使用 atexit 模块
# 调用 register 函数, 便可以将函数注册为终止函数
# 也可以添加更多的参数, 这些将作为 exit 函数的参数传递.

import atexit
def exit(*args):
	print('exit',args)
atexit.register(exit)
atexit.register(exit,1)
atexit.register(exit,'hello','world')


'''
exit ('hello', 'world')
exit (1,)
exit ()
'''

# 该模块其实是一个对 sys.exitfunc 钩子( hook )的简单封装.