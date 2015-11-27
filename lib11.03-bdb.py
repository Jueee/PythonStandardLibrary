'''
bdb 模块

bdb 模块为提供了一个调试器框架. 你可以使用它来创建自定义的调试器

需要做的只是继承  Bdb 类, 覆盖它的 user 方法(在每次调试器停止的时候被调用). 
使用各种各样的 set 方法可以控制调试器.
'''
import bdb
import time

def spam(n):
	j = 0
	for i in range(n):
		j = j + i
	return n
def egg(n):
	spam(n)
	spam(n)
	spam(n)
	spam(n)
def test(n):
	egg(n)
class myDebugger(bdb.Bdb):
	run = 0
	def user_call(self, frame, args):
		name = frame.f_code.co_name or "<unknown>"
		print("call", name, args)
		self.set_continue() # continue
	def user_line(self, frame):
		if self.run:
			self.run = 0
			self.set_trace() # start tracing
		else:
			# arrived at breakpoint
			name = frame.f_code.co_name or "<unknown>"
			filename = self.canonic(frame.f_code.co_filename)
			print("break at", filename, frame.f_lineno, "in", name)
		print("continue...")
		self.set_continue() # continue to next breakpoint
	def user_return(self, frame, value):
		name = frame.f_code.co_name or "<unknown>"
		print("return from", name, value)
		print("continue...")
		self.set_continue() # continue
	def user_exception(self, frame, exception):
		name = frame.f_code.co_name or "<unknown>"
		print("exception in", name, exception)
		print("continue...")
		self.set_continue() # continue
db = myDebugger()
db.run = 1
db.set_break("lib11.03-bdb.py", 7)
db.runcall(test, 1)

