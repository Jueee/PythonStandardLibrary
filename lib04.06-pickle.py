'''
pickle 模块

pickle 模块同 marshal 模块相同, 将数据连续化, 便于保存传输. 
它比marshal 要慢一些, 但它可以处理类实例, 共享的元素, 以及递归数据结构等.
'''
# 使用 pickle 模块
import pickle

value = (
	"this is a string",
	[1, 2, 3, 4],
	("more tuples", 1.0, 2.3, 4.5),
	"this is yet another string"
	)
data = pickle.dumps(value)

# intermediate format
print(type(data), len(data))

print("-"*50)
print(data)
print("-"*50)

print(pickle.loads(data))







# 使用 pickle 模块的二进制模式
# pickle 使用急于文本的格式. 你也可以使用二进制格式, 这样数字和二进制字符串就会以紧密的格式储存, 这样文件就会更小点. 
import pickle
import math

value = (
	"this is a long string" * 100,
	[1.2345678, 2.3456789, 3.4567890] * 100
	)

# text mode
data = pickle.dumps(value)
print(type(data), len(data), pickle.loads(data) == value)

# binary mode
data = pickle.dumps(value, 1)
print(type(data), len(data), pickle.loads(data) == value)


