'''
Queue 模块

Queue 模块提供了一个线程安全的队列 (queue) 实现.
可以通过它在多个线程里安全访问同个对象.
'''
import threading
import queue
import time, random

WORKERS = 2

class Worker(threading.Thread):
	"""docstring for Worker"""
	def __init__(self, queue):
		self.__queue = queue
		threading.Thread.__init__(self)
	def run(self):
		while 1:
			item = self.__queue.get()
			if item is None:
				break
			time.sleep(random.randint(10, 100) / 1000.0)
			print('task', item, 'finished')

queue = queue.Queue(0)
		
for i in range(WORKERS):
	Worker(queue).start()	# start a worker

for i in range(10):
	queue.put(i)

for i in range(WORKERS):
	queue.put(None)			# add end-of-queue markers





# 使用限制大小的 Queue 模块
# 如果队列满了, 那么控制主线程 (producer threads) 被阻塞, 等待项目被弹出 (pop off).
import threading
import queue
import time, random

WORKERS = 2

class Worker(threading.Thread):
	"""docstring for Worker"""
	def __init__(self, queue):
		self.__queue = queue
		threading.Thread.__init__(self)
	def run(self):
		while 1:
			item = self.__queue.get()
			if item is None:
				break
			time.sleep(random.randint(10, 100) / 1000.0)
			print('task', item, 'finished')

# run with limited queue
queue = queue.Queue(3)
		
for i in range(WORKERS):
	Worker(queue).start()	# start a worker

for i in range(10):
	print('push', i)
	queue.put(i)

for i in range(WORKERS):
	queue.put(None)			# add end-of-queue markers






# 使用 Queue 模块实现优先级队列
# 可以通过继承 Queue 类来修改它的行为. 
# 它接受一个元组作为参数, 元组的第一个成员表示优先级(数值越小优先级越高).
'''
import queue
import bisect

Empty = queue.Empty

class PriorityQueue(queue.Queue):
	"""Thread-safe priority queue"""
	def _put(self, item):
		bisect.insort(self.queue, item)

queue = PriorityQueue(0)

# add items out of order
queue.put((20, 'second'))
queue.put((10, 'first'))
queue.put((30, 'third'))

# print queue contents
try:
	while 1:
		print(queue.get_nowait())
except Empty:
	pass
'''





# 使用 Queue 模块实现一个堆栈
# 一个简单的堆栈 (stack) 实现 (末尾添加, 头部弹出, 而非头部添加, 头部弹出).
import queue

Empty = queue.Empty

class Stack(queue.Queue):
	"""Thread-safe stack"""
	def __init__(self, arg):
		super(Stack, self).__init__()
		self.arg = arg
		