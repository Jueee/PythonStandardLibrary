'''
operator 模块

operator 模块为 Python 提供了一个 "功能性" 的标准操作符接口. 
当使用 map 以及 filter 一类的函数的时候, operator 模块中的函数可以替换一些 lambda 函式. 
'''

# 使用 operator 模块
import operator
from functools import reduce
'''
在Python 3里，reduce()函数已经被从全局名字空间里移除了，它现在被放置在fucntools模块里
用的话要 先引入
from functools import reduce
'''
help(operator)
sequence = 1, 2, 4
print("add", "=>", reduce(operator.add, sequence))
print("sub", "=>", reduce(operator.sub, sequence))
print("mul", "=>", reduce(operator.mul, sequence))
print("concat", "=>", operator.concat("spam", "egg"))
#print("repeat", "=>", .repeat("spam", 5))
print("getitem", "=>", operator.getitem(sequence, 2))
print("indexOf", "=>", operator.indexOf(sequence, 2))
#print("sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 3))



'''
# 使用 operator 模块检查类型
import operator
import UserList
def dump(data):
	print(type(data), "=>",end='')
	if operator.isCallable(data):
		print("CALLABLE",end='')
	if operator.isMappingType(data):
		print("MAPPING",end='')
	if operator.isNumberType(data):
		print("NUMBER",end='')
	if operator.isSequenceType(data):
		print("SEQUENCE",end='')
	print()
dump(0)
dump("string")
dump("string"[0])
dump([1, 2, 3])
dump((1, 2, 3))
dump({"a": 1})
dump(len) # function 函数
dump(UserList) # module 模块
dump(UserList.UserList) # class 类
dump(UserList.UserList()) # instance 实例
'''




