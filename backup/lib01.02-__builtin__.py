# 包含 Python 中使用的内建函数. 一般不用手动导入这个模块

# 全局函数apply()
'''
Python 2有一个叫做apply()的全局函数，它使用一个函数f和一个列表[a, b, c]作为参数，返回值是f(a, b, c)。
也可以通过直接调用这个函数，在列表前添加一个星号(*)作为参数传递给它来完成同样的事情。
在Python 3里，apply()函数不再存在了；必须使用星号标记法。
'''
def function(a,b):
	print(a,b)

'''
apply(function,("whither","canada?"))
apply(function,(1,2+3))
'''

function(*("whither","canada?"))
function(*(1,2+3))

# 可以通过在参数列表前添加一个星号(*)，在字典命名参数前添加两个星号(**)来达到同样的效果。
function(**{"a": "crunchy", "b": "frog"})



# dir 返回由给定模块, 类, 实例, 或其他类型的所有成员组成的列表.
def dump(value):
	print(value,"=>",dir(value))

dump(0)
dump(1.0)
dump(0.0j)	#虚数
dump([])	#列表
dump({})	#字典
dump('string')	#字符串
dump(len)	#函数
dump(dump)





# 使用 dir 函数查找类的所有成员
print('-------')

class A:
	def a(self):
		pass
	def b(self):
		pass
class B(A):
	def c(self):
		pass
	def d(self):
		pass
#  getmembers 函数返回了一个有序列表. 成员在列表中名称出现的越早, 它所处的类层次就越高. 
def getmembers(klass, members=None):
	# get a list of all class members, ordered by class
	if members is None:
		members = []
	for k in klass.__bases__:
		getmembers(k, members)
	for m in dir(klass):
		if m not in members:
			members.append(m)
	return members
print(getmembers(A))
print(getmembers(B))
print(getmembers(IOError))


# vars 函数与此相似, 它返回的是包含每个成员当前值的字典. 
# 如果你使用不带参数的 vars , 它将返回当前局部名称空间的可见元素
book = "library2"
pages = 250
scripts = 350
print("the %(book)s book contains more than %(scripts)s scripts" % vars())



# Python 是一种动态类型语言, 这意味着给一个定变量名可以在不同的场合绑定到不同的类型上.
# type 函数允许你检查一个变量的类型.
# 可以使用 is 操作符 (对象身份?)来检查类型
def function(value):
	if isinstance(value,float):
		print("this is float")
	print(value,type(value))
function(1)
function(1.0)
function("one")



def load(file):
	print("文件类型为：",type(file))
	if isinstance(file, type("")):
		file = open(file, "rb")
	return file.read()
print(len(load("samples/sample.jpg")), "bytes")
print(len(load(open("samples/sample.jpg", "rb"))), "bytes")


# callable 函数, 可以检查一个对象是否是可调用的(无论是直接调用或是通过 apply ).
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True.
def dump(function):
	if callable(function):
		print(function, "is callable")
	else:
		print(function, "is *not* callable")
class A:
	def method(self, value):
		return value
class B(A):
	def __call__(self, value):
		return value2
a = A()
b = B()
dump(0) # simple objects
dump("string")
dump(callable)
dump(dump) # function
dump(A) # classes
dump(B)
dump(B.method)
dump(a) # instances
dump(b)
dump(b.method)
'''
0 is *not* callable
string is *not* callable
<built-in function callable> is callable
<function dump at 0x02B2F3D8> is callable
<class '__main__.A'> is callable
<class '__main__.B'> is callable
<function A.method at 0x02B2F1E0> is callable
<__main__.A object at 0x02B15F10> is *not* callable
<__main__.B object at 0x02B15ED0> is callable
<bound method B.method of <__main__.B object at 0x02B15ED0>> is callable
'''


#  eval 函数将一个字符串作为 Python 表达式求值. 
def dump(expression):
	result = eval(expression)
	print(expression, "=>", result, type(result))
dump("1")
dump("1.0")
dump("'string'")
dump("1.0 + 2.0")
dump("'*' * 10")
dump("len('world')")
'''
1 => 1 <class 'int'>
1.0 => 1.0 <class 'float'>
'string' => string <class 'str'>
1.0 + 2.0 => 3.0 <class 'float'>
'*' * 10 => ********** <class 'str'>
len('world') => 5 <class 'int'>
'''


# eval 函数只针对简单的表达式. 如果要处理大块的代码, 你应该使用 compile 和 exec 函数




'''
在Python 3里，execfile语句已经被去掉了。
如果你真的想要执行一个文件里的Python代码(但是你不想导入它)，你可以通过打开这个文件，读取它的内容，然后调用compile()全局函数强制Python解释器编译代码，然后调用新的exec()函数。

Python 2：execfile('a_filename')	
Python 3：exec(compile(open('a_filename').read(),'a_filename','exec'))

'''
# execfile("hello.py")
def EXECFILE(filename):
	exec(compile(open(filename).read(),filename,'exec'))

EXECFILE("hello.py")





'''
从 __builtin__ 模块重载函数
因为 Python 在检查局部名称空间和模块名称空间前不会检查内建函数, 所以有时候你可能要显式地引用 _ _builtin_ _ 模块. 
例如下面重载了内建的 open 函数. 这时候要想使用原来的 open 函数, 就需要脚本显式地指明模块名称.
'''
# 在Python2.X版本中，内建模块被命名为__builtin__，而到了Python3.X版本中，却更名为builtins。
def open(filename, mode="rb"):
	import builtins
	file = builtins.open(filename, mode)
	print("file.read(5):",file.read(5))
	if file.read(5) not in("GIF87", "GIF89"): 
		print("not a GIF file")
	file.seek(0) 
	return file

fp = open("samples/sample.gif")
print(len(fp.read()), "bytes")
fp = open("samples/sample.jpg") 
print(len(fp.read()), "bytes")
