'''
dis 模块

dis 模块是 Python 的反汇编器. 它可以把字节码转换为更容易让人看懂的格式.

可以从命令行调用反汇编器. 
它会编译给定的脚本并把反汇编后的字节代码输出到终端上.


dis 也可以作为模块使用. 
dis 函数接受一个类, 方法, 函数, 或者 code 对象作为单个参数.
'''
import dis

def procedure():
	print('hello')

dis.dis(procedure)

'''
 16           0 LOAD_GLOBAL              0 (print) 
              3 LOAD_CONST               1 ('hello') 
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair) 
              9 POP_TOP              
             10 LOAD_CONST               0 (None) 
             13 RETURN_VALUE         
[Finished in 0.2s]
'''