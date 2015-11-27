'''
pdb 模块

pdb 模块是标准 Python 调试器( debugger ). 它基于 bdb 调试器框架.
'''
import pdb

def test(n):
	j = 0
	for i in range(n):
		j = j + i
	return n

db = pdb.Pdb()
db.runcall(test, 1)

'''
> e:\360\python\pythoncode\01study\03-standardlibrary\lib11.02-pdb.py(9)test()
-> j = 0
(Pdb) 
[Finished in 0.3s]
'''