'''
thread 模块

(可选) thread 模块提为线程提供了一个低级 (low_level) 的接口

只有你在编译解释器时打开了线程支持才可以使用它. 
如果没有特殊需要, 最好使用高级接口 threading 模块替代.

python3 中改名为_thread


[注]当主程序退出的时候, 所有的线程也随着退出. 
而 threading 模块不存在这个问题 .
'''
import _thread
import time, random

def worker():
	for i in range(50):
		time.sleep(random.randint(10, 100) / 1000.0)
		print(_thread.get_ident(), '- task', i, 'finished')

for i in range(2):
	_thread.start_new_thread(worker, ())

time.sleep(1)

print('goodbye !')



