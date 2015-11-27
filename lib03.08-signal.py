'''
signal 模块

可以使用 signal 模块配置你自己的信号处理器 (signal handler). 
当解释器收到某个信号时, 信号处理器会立即执行.


alarm() -- cause SIGALRM after a specified time [Unix only]
'''
import signal
import time

def handler(signo, frame):
	print('got signal', signo)

help(signal)
signal.signal(signal.SIGALRM, handler)

signal.alarm(2)

now = time.time()

time.sleep(200)

print('slept for', time.time() - now , 'seconds')




