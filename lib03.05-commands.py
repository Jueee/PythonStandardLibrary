'''
commands 模块


(只用于 Unix) commands 模块包含一些用于执行外部命令的函数. 
'''

import commands

stat, output = commands.getstatusoutput("ls -lR")
print("status", "=>", stat)
print("output", "=>", len(output), "bytes")

'''
status => 0
output => 171046 bytes
'''