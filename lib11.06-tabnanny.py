'''
tabnanny 模块

(2.0 新增) tabnanny 模块用于检查 Python 源文件中的含糊的缩进. 
当文件混合了 tab 和空格两种缩进时候, nanny (保姆)会立即给出提示.


在下边使用的 badtabs.py 文件中, if 语句后的第一行使用 4 个空格和 1 个tab . 第二行只使用了空格.
$ tabnanny.py -v samples/badtabs.py
';samples/badtabs.py': *** Line 3: trouble in tab city! ***
offending line: print "world"
indent not equal e.g. at tab sizes 1, 2, 3, 5, 6, 7, 9

因为 Python 解释器把 tab 作为 8 个空格来处理, 所以这个脚本可以正常运行. 
在所有符合代码标准(一个 tab 为 8 个空格)的编辑器中它也会正常显示.
当然, 这些都骗不过 nanny .

'''
import tabnanny

FILE = 'samples/badtabs.py'

file = open(FILE)
for line in file.readlines():
	print(line)

tabnanny.check(FILE)