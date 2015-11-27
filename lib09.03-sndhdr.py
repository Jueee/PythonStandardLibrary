'''
sndhdr 模块

sndhdr 模块, 可来识别不同的音频文件格式, 并提取文件内容相关信息. 

执行成功后, what 函数将返回一个由文件类型, 采样频率, 声道数, 音轨数和
每个采样点位数组成的元组. 具体含义请参考 help(sndhdr) .
'''
import sndhdr

result = sndhdr.what('samples/sample.wav')

if result:
	print('file format:', result)
else:
	print('connot identify file')

	