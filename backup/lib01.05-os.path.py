'''
os.path 模块

os.path 模块包含了各种处理长文件名(路径名)的函数. 
先导入 (import) os模块, 然后就可以以 os.path 访问该模块.
'''

'''
处理文件名

os.path 模块包含了许多与平台无关的处理长文件名的函数. 
也就是说, 你不需要处理前后斜杠, 冒号等.
'''
# 使用 os.path 模块处理文件名
import os
filename = "E:\\360\\Python\\PythonCode\\01Study\\03-StandardLibrary"
print('using',os.name,'...')
print('split','=>',os.path.split(filename))
print('splitext','=>',os.path.splitext(filename))
print('dirname','=>',os.path.dirname(filename))
print('basename','=>',os.path.basename(filename))
print('join','=>',os.path.join(os.path.dirname(filename),os.path.basename(filename)))

'''
using nt ...
split => ('E:\\360\\Python\\PythonCode\\01Study', '03-StandardLibrary')
splitext => ('E:\\360\\Python\\PythonCode\\01Study\\03-StandardLibrary', '')
dirname => E:\360\Python\PythonCode\01Study
basename => 03-StandardLibrary
join => E:\360\Python\PythonCode\01Study\03-StandardLibrary
'''



# 使用 os.path 模块检查文件名的特征
# os.path 模块中还有许多函数允许你简单快速地获知文件名的一些特征
import os
FILES = (
	os.curdir,
	"/",
	"file",
	"/file",
	"samples",
	"samples/sample.jpg",
	"directory/file",
	"../directory/file",
	"/directory/file",
	"C:/"
	)
for file in FILES:
	print(file, "=>",end='')
	if os.path.exists(file): # 判断文件是否存在
		print("EXISTS ",end='')
	if os.path.isabs(file):#判断是否为绝对路径
		print("ISABS ",end='')
	if os.path.isdir(file):#判断路径是否为目录
		print("ISDIR ",end='')
	if os.path.isfile(file):#判断路径是否为文件
		print("ISFILE ",end='')
	if os.path.islink(file): #判断路径是否为链接
		print("ISLINK ",end='')
	if os.path.ismount(file):#判断路径是否为挂载点（挂载点实际上就是linux中的磁盘文件系统的入口目录,类似于windows中的用来访问不同分区的C:、D:、E:等盘符。）
		print("ISMOUNT ",end='')
	print(" => over")
'''
. =>EXISTS ISDIR  => over
/ =>EXISTS ISABS ISDIR ISMOUNT  => over
file => => over
/file =>ISABS  => over
samples =>EXISTS ISDIR  => over
samples/sample.jpg =>EXISTS ISFILE  => over
directory/file => => over
../directory/file => => over
/directory/file =>ISABS  => over
C:/ =>EXISTS ISABS ISDIR ISMOUNT  => over
'''





# 使用 os.path 模块将用户名插入到文件名
# expanduser 函数以与大部分Unix shell相同的方式处理用户名快捷符号(~, 不过在 Windows 下工作不正常)
import os
print(os.path.expanduser("~/.pythonrc"))




# 使用 os.path 替换文件名中的环境变量
import os
os.environ["USER"] = "wyq10580"
print(os.path.expandvars("/home/$USER/config"))
print(os.path.expandvars("$USER/folders"))




'''
搜索文件系统
'''
# 使用 os.path 搜索文件系统
# walk 函数会帮你找出一个目录树下的所有文件. 
# 它的参数依次是目录名, 回调函数, 以及传递给回调函数的数据对象.
'''
python 2.X

import os
def callback(arg,directory,files):
	print(files)
	for file in files:
		print(os.path.join(directory,file),repr(arg))

os.path.walk(r"E:\\360\\Python\\PythonCode\\01Study\\03-StandardLibrary", callback, 'secret message')
'''





# 使用 os.listdir 搜索文件系统
# 
import os
def index(directory):
	# like os.listdir, but traverses directory trees
	stack = [directory]
	files = []
	while stack:
		directory = stack.pop()
		for file in os.listdir(directory):
			fullname = os.path.join(directory, file)
			files.append(fullname)
			if os.path.isdir(fullname) and not os.path.islink(fullname):
				stack.append(fullname)
	return files

print('--- os.listdir --')
for file in index("."):
	print(file)




# 使用 DirectoryWalker 搜索文件系统
import os
class DirectoryWalker:
	# a forward iterator that traverses a directory tree
	def __init__(self, directory):
		self.stack = [directory]
		self.files = []
		self.index = 0
	def __getitem__(self, index):
		while 1:
			try:
				file = self.files[self.index]
				self.index = self.index + 1
			except IndexError:
				# pop next directory from stack
				self.directory = self.stack.pop()
				self.files = os.listdir(self.directory)
				self.index = 0
			else:
				# got a filename
				fullname = os.path.join(self.directory, file)
				if os.path.isdir(fullname) and not os.path.islink(fullname):
					self.stack.append(fullname)
				return fullname

print('-- DirectoryWalker --')
for file in DirectoryWalker("."):
	print(file)





#  使用 DirectoryStatWalker 搜索文件系统
import os, stat
class DirectoryStatWalker:
	# a forward iterator that traverses a directory tree, and
	# returns the filename and additional file information
	def __init__(self, directory):
		self.stack = [directory]
		self.files = []
		self.index = 0
	def __getitem__(self, index):
		while 1:
			try:
				file = self.files[self.index]
				self.index = self.index + 1
			except IndexError:
				# pop next directory from stack
				self.directory = self.stack.pop()
				self.files = os.listdir(self.directory)
				self.index = 0
			else:
				# got a filename
				fullname = os.path.join(self.directory, file)
				st = os.stat(fullname)
				mode = st[stat.ST_MODE]
				if stat.S_ISDIR(mode) and not stat.S_ISLNK(mode):
					self.stack.append(fullname)
				return fullname, st
print('-- DirectoryStatWalker --')
for file, st in DirectoryStatWalker("."):
	print(file, st[stat.ST_SIZE])




