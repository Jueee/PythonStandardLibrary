'''
filecmp 模块
( 2.0 新增) filecmp 模块用于比较文件和目录
'''

import filecmp

if filecmp.cmp('samples/sample.au', 'samples/sample.wav'):
	print('files are identical')
else:
	print('files differ!')

'''
files differ!
[Finished in 0.3s]
'''