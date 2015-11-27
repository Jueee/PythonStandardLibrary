'''
threading 模块

(可选) threading 模块为线程提供了一个高级接口

它源自 Java 的线程实现. 
和低级的 thread 模块相同, 只有你在编译解释器时打开了线程支持才可以使用它.

你只需要继承  Thread 类, 定义好 run 方法, 就可以创建一个新的线程. 
使用时首先创建该类的一个或多个实例, 然后调用 start 方法. 
这样每个实例的 run 方法都会运行在它自己的线程里.
'''

# 使用 threading 模块
import threading
import time, random

class Counter(object):
	"""docstring for Counter"""
	def __init__(self): 
		# 使用了  Lock 对象来在全局  Counter 对象里创建临界区(critical section). 
		self.lock = threading.Lock()
		self.value = 0
	def increment(self):
		self.lock.acquire()
		self.value = value = self.value + 1
		self.lock.release()
		return value

counter = Counter()


class Worker(threading.Thread):
	"""docstring for Worker"""
	def run(self):
		# pretend we're doing something that takes 10?00 ms
		value = counter.increment()     # increment global counter
		time.sleep(random.randint(10, 100) / 1000.0)
		print(self.getName(), '-- task', i, 'finished', value)


# try it
for i in range(10):
	Worker().start()       # start a worker