'''
nt 模块

(非直接使用模块, 只用于 Windows ) nt 模块是 os 模块在 Windows 平台下调用的执行模块. 

几乎没有任何原因直接使用这个模块, 请使用 os 模块替代.
'''
import nt

for file in nt.listdir('.'):
	print(file, '=>', nt.stat(file)[6], '=>', nt.stat(file))