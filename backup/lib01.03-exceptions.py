# exceptions 模块提供了标准异常的层次结构.

# Python 启动的时候会自动导入这个模块


'''
该模块定义了以下标准异常：

•  Exception 是所有异常的基类. 强烈建议(但不是必须)自定义的异常异常也继承这个类.
•  SystemExit(Exception) 由 sys.exit 函数引发. 如果它在最顶层没有被 try-except 语句捕获, 那么解释器将直接关闭而不会显示任何跟踪返回信息.
•  StandardError(Exception) 是所有内建异常的基类(除  SystemExit外).
•  KeyboardInterrupt(StandardError) 在用户按下 Control-C(或其他打断按键)后被引发. 如果它可能会在你使用 "捕获所有" 的 try-except语句时导致奇怪的问题.
•  ImportError(StandardError) 在 Python 导入模块失败时被引发.
•  EnvironmentError 作为所有解释器环境引发异常的基类. (也就是说,这些异常一般不是由于程序 bug 引起).
•  IOError(EnvironmentError) 用于标记 I/O 相关错误.
•  OSError(EnvironmentError) 用于标记 os 模块引起的错误.
•  WindowsError(OSError) 用于标记 os 模块中 Windows 相关错误.
•  NameError(StandardError) 在 Python 查找全局或局部名称失败时被引发.
•  UnboundLocalError(NameError) , 当一个局部变量还没有赋值就被使用时, 会引发这个异常. 这个异常只有在 2.0 及之后的版本有; 早期版本只会引发一个普通的  NameError .
•  AttributeError(StandardError) , 当 Python 寻找(或赋值)给一个实例属性, 方法, 模块功能或其它有效的命名失败时, 会引发这个异常.
•  SyntaxError(StandardError) , 当解释器在编译时遇到语法错误, 这个异常就被引发.
•  (2.0 及以后版本)  IndentationError(SyntaxError) 在遇到非法的缩进时被引发. 该异常只用于 2.0 及以后版本, 之前版本会引发一个SyntaxError 异常.
•  (2.0 及以后版本)  TabError(IndentationError) , 当使用 -tt 选项检查不一致缩进时有可能被引发. 该异常只用于 2.0 及以后版本, 之前版本会引发一个  SyntaxError 异常.
•  TypeError(StandardError) , 当给定类型的对象不支持一个操作时被引发.
•  AssertionError(StandardError) 在 assert 语句失败时被引发(即表达式为 false 时).
•  LookupError(StandardError) 作为序列或字典没有包含给定索引或键时所引发异常的基类.
•  IndexError(LookupError) , 当序列对象使用给定索引数索引失败时(不存在索引对应对象)引发该异常.
•  KeyError(LookupError) 当字典对象使用给定索引索引失败时(不存在索引对应对象)引发该异常.
•  ArithmeticError(StandardError) 作为数学计算相关异常的基类.
•  OverflowError(ArithmeticError) 在操作溢出时被引发(例如当一个整数太大, 导致不能符合给定类型).
•  ZeroDivisionError(ArithmeticError) , 当你尝试用 0 除某个数时被引发.
•  FloatingPointError(ArithmeticError) , 当浮点数操作失败时被引发.
•  ValueError(StandardError) , 当一个参数类型正确但值不合法时被引发.
•  (2.0 及以后版本)  UnicodeError(ValueError) , Unicode 字符串类型相关异常. 只使用在 2.0 及以后版本.
•  RuntimeError(StandardError) , 当出现运行时问题时引发, 包括在限制模式下尝试访问外部内容, 未知的硬件问题等等.
•  NotImplementedError(RuntimeError) , 用于标记未实现的函数, 或无效的方法.
•  SystemError(StandardError) , 解释器内部错误. 该异常值会包含更多的细节 (经常会是一些深层次的东西, 比如 "eval_code2: NULL
globals" ) . 这本书的作者编了 5 年程序都没见过这个错误. (想必是没有用 raise SystemError ).
•  MemoryError(StandardError) , 当解释器耗尽内存时会引发该异常. 注意只有在底层内存分配抱怨时这个异常才会发生; 如果是在你的旧机器上, 这个异常发生之前系统会陷入混乱的内存交换中.
'''


class HTTPError(Exception):
	# indicates an HTTP protocol error
	def __init__(self, url, errcode, errmsg):
		self.url = url
		self.errcode = errcode
		self.errmsg = errmsg 
	def __str__(self):
		return ( "<HTTPError for %s: %s %s>" % (self.url,self.errcode, self.errmsg)) 


try:
	raise HTTPError("http://www.python.org/foo", 200, "NotFound") 
except HTTPError as error: 
	print("url", "=>", error.url)
	print("errcode", "=>", error.errcode)
	print("errmsg", "=>", error.errmsg) 
	raise #reraise exception