'''
repr 模块

repr 模块提供了内建 repr 函数的另个版本. 
它限制了很多(字符串长度, 递归等).
'''
# an annoyingly recursive data structure
data = (
	"X" * 100000,
	)
data = [data]
data.append(data)
print(repr(data))

