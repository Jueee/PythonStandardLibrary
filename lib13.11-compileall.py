'''
compileall 模块

compileall 模块用于将给定目录下(以及 Python path )的所有 Python 脚本编译为字节代码. 
它也可以作为可执行脚本使用(在 Unix 系统下, Python 安装时会自动调用执行它). 
'''
import compileall

print('This may take a while !')

compileall.compile_dir('.', force = 1)