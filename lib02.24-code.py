'''
code 模块

code 模块提供了一些用于模拟标准交互解释器行为的函数.

compile_command 与内建 compile 函数行为相似, 但它会通过测试来保证你传递的是一个完成的 Python 语句.
'''
a = (1, 2, 3)
print(a)


# 使用 code 模块编译语句
import code

SCRIPT = ['a=(', '1,' '2,' '3', ')', 'print(a)']
script = ''
for line in SCRIPT:
	script = script + line + '\n'
	co = code.compile_command(script, '<stdin>', 'exec')
	if co:
		# got a complete statement. execute it!
		print('-' * 40)
		print(script)
		print('-' * 40)
		exec(co)
		script = ''





# 使用 code 模块模拟交互解释器
# InteractiveConsole 类实现了一个交互控制台, 类似你启动的 Python 解释器交互模式.
# 控制台可以是活动的(自动调用函数到达下一行) 或是被动的(当有新数据时调用  push 方法). 
# 默认使用内建的 raw_input 函数. 如果你想使用另个输入函数, 你可以使用相同的名称重载这个方法.
import code

console = code.InteractiveConsole()
#console.interact()



print('---------------------------------------')


# 使用 code 模块实现简单的 Debugging
# keyboard 函数. 它允许你在程序中手动控制交互解释器.
def keyboard(banner = None):
	import code, sys
	# use exception trick to pick up the current frame
	try:
		raise(None)
	except:
		frame = sys.exc_info()[2].tb_frame.f_back
	# evaluate commands in current namespace
	namespace = frame.f_globals.copy()
	namespace.update(frame.f_locals)
	code.interact(banner = banner, local = namespace)

def func():
	print('START')
	a = 10
	keyboard()
	print('END')

func()