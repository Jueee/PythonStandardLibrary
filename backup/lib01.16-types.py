'''
types 模块

types 模块包含了标准解释器定义的所有类型的类型对象

同一类型的所有对象共享一个类型对象. 
可以使用 is 来检查一个对象是不是属于某个给定类型.
'''
'''
types模块中的常量#
types模块里各种各样的常量能帮助你决定一个对象的类型。
在Python 2里，它包含了代表所有基本数据类型的常量，如dict和int。
在Python 3里，这些常量被已经取消了。只需要使用基础类型的名字来替代。

	Python 2					Python 3
 	types.UnicodeType			str
 	types.StringType			bytes
 	types.DictType				dict
 	types.IntType				int
 	types.LongType				int
 	types.ListType				list
 	types.NoneType				type(None)
 	types.BooleanType			bool
 	types.BufferType			memoryview
 	types.ClassType				type
 	types.ComplexType			complex
 	types.EllipsisType			type(Ellipsis)
 	types.FloatType				float
 	types.ObjectType			object
 	types.NotImplementedType	type(NotImplemented)
 	types.SliceType				slice
 	types.TupleType				tuple
 	types.TypeType				type
 	types.XRangeType			range
☞types.StringType被映射为bytes，而非str，因为Python 2里的“string”(非Unicode编码的字符串，即普通字符串)事实上只是一些使用某种字符编码的字节序列(a sequence of bytes)。
'''
def check(object):
	print(object,type(object),'=>','',end='')
	if type(object) is int:
		print("INTEGER",end='')
	if type(object) is float:
		print("FLOAT",end='')
	if type(object) is bytes:
		print("STRING",end='')
	if type(object) is type:
		print("CLASS",end='')
	if type(object) is str:
		print("STRING",end='')
	if type(object) is object:
		print("STRING",end='')
#	if type(object) is instance:
#		print("INSTANCE",end='')
	print()
check(0)
check(0.0)
check("0")
class A:
	pass
class B:
	pass
check(A)
check(B)
a = A()
b = B()
check(a)
check(b)

'''
0 <class 'int'> => INTEGER
0.0 <class 'float'> => FLOAT
0 <class 'str'> => STRING
<class '__main__.A'> <class 'type'> => CLASS
<class '__main__.B'> <class 'type'> => CLASS
<__main__.A object at 0x02C17B70> <class '__main__.A'> => 
<__main__.B object at 0x02C17B30> <class '__main__.B'> => 
'''

