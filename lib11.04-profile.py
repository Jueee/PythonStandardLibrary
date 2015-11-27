'''
profile 模块

profile 模块是标准 Python 分析器.

和反汇编器, 调试器相同, 你可以从命令行调用分析器
'''
# U 使用 profile 模块
import profile

def func1():
	for i in range(1000):
		pass

def func2():
	for i in range(1000):
		func1()

profile.run('func2()')

'''
         1005 function calls in 0.062 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.047    0.047 :0(exec)
        1    0.016    0.016    0.016    0.016 :0(setprofile)
        1    0.000    0.000    0.047    0.047 <string>:1(<module>)
     1000    0.047    0.000    0.047    0.000 lib11.04-profile.py:11(func1)
        1    0.000    0.000    0.047    0.047 lib11.04-profile.py:15(func2)
        1    0.000    0.000    0.062    0.062 profile:0(func2())
        0    0.000             0.000          profile:0(profiler)


'''