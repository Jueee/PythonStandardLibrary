'''
pstats 模块

pstats 模块用于分析 Python 分析器收集的数据.
'''
import pstats
import profile

def func1():
	for i in range(1000):
		pass

def func2():
	for i in range(1000):
		func1()

p = profile.Profile()
p.run('func2()')

#profile.run('func2()')

s = pstats.Stats(p)
s.sort_stats('time', 'name').print_stats()

'''
         1005 function calls in 0.031 seconds

   Ordered by: internal time, function name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.031    0.000    0.031    0.000 E:\360\Python\PythonCode\01Study\03-StandardLibrary\lib11.05-pstats.py:9(func1)
        1    0.000    0.000    0.031    0.031 <string>:1(<module>)
        1    0.000    0.000    0.031    0.031 :0(exec)
        1    0.000    0.000    0.031    0.031 E:\360\Python\PythonCode\01Study\03-StandardLibrary\lib11.05-pstats.py:13(func2)
        1    0.000    0.000    0.031    0.031 profile:0(func2())
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.000    0.000 :0(setprofile)


[Finished in 0.3s]
'''