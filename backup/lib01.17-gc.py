'''
gc 模块

gc 模块提供了到内建循环垃圾收集器的接口.

Python 使用引用记数来跟踪什么时候销毁一个对象; 一个对象的最后一个引用一旦消失, 这个对象就会被销毁.

从 2.0 版开始, Python 还提供了一个循环垃圾收集器, 它每隔一段时间执行.
这个收集器查找指向自身的数据结构, 并尝试破坏循环.
'''


# 使用 gc 模块收集循环引用垃圾
# 可以使用 gc.collect 函数来强制完整收集. 
# 这个函数将返回收集器销毁的对象的数量.
import gc

class Node(object):
	"""docstring for Node"""
	def __init__(self, name):
		super(Node, self).__init__()
		self.name = name
		self.parent = None
		self.children = []
	def addchild(self,node):
		node.parent = self
		self.children.append(node)
	def __repr__(self):
		return '<Node %s at %x>' % (repr(self.name),id(self))

root = Node('monty')

root.addchild(Node('eric'))
root.addchild(Node('john'))
root.addchild(Node('michael'))

del root

print(gc.collect(),'unreachable objects')
print(gc.collect(),'unreachable objects')

'''
12 unreachable objects
0 unreachable objects
'''