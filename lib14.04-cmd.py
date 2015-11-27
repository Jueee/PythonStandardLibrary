'''
cmd 模块

cmd 模块为命令行接口( command-line interfaces , CLI )提供了一个简单的
框架. 

只需要继承  Cmd 类, 定义 do 和 help 方法. 基类会自动地将这些方法转换
为对应命令.
'''
import cmd
import sys

class CLI(cmd.Cmd):
	"""docstring for CLI"""
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = ' > '
	def do_hello(self, arg):
	 	print('hello again', arg, '!')
	def help_hello(self):
		print('syntax:hello[message]', end = '')
		print('-- prints a hello message')
	def do_quit(self, arg):
		sys.exit(1)
	def help_quit(self):
		print('syntax:quit', end = '')
		print('-- terminates the application')
	do_q = do_quit

cli = CLI()
cli.cmdloop()