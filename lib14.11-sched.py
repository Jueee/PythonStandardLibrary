'''
sched 模块
sched 模块为非线程环境提供了一个简单的计划任务模式. 
'''
import sched
import time,sys

scheduler = sched.scheduler(time.time, time.sleep)

# add a few operations to the queue
scheduler.enter(0.5, 100, sys.stdout.write, ('one\n',))
scheduler.enter(1.0, 300, sys.stdout.write, ('three\n',))
scheduler.enter(1.0, 100, sys.stdout.write, ('two\n',))

scheduler.run()