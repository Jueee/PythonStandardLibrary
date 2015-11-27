'''
mailcap 模块

mailcap 模块用于处理  mailcap 文件, 该文件指定了不同的文档格式的处理方法( Unix 系统下). 
'''
# 使用 mailcap 模块获得 Capability 字典
import mailcap

caps = mailcap.getcaps()
print(caps)

for k, v in caps.items():
	print(k, '=', v)




# 使用 mailcap 模块获得打开
import mailcap
caps = mailcap.getcaps()
command, info = mailcap.findmatch(
	caps, "image/jpeg", "view", "samples/sample.jpg"
	)
print(command)