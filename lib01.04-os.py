# 这个模块中的大部分函数通过对应平台相关模块实现
# 比如 posix 和 nt. os模块会在第一次导入的时候自动加载合适的执行模块.


'''
处理文件


内建的 open / file 函数用于创建, 打开和编辑文件
'''
# 使用 os 模块重命名和删除文件
import os 

def replace(file, search_for, replace_with):
	print(os.path.splitext(file)[0])
	back = os.path.splitext(file)[0] + ".bak"
	temp = os.path.splitext(file)[0] + ".tmp"
	try:
		# # remove old temp file, if any
		os.remove(temp)
	except os.error:
		pass
	fi = open(file)
	fo = open(temp, "w")
	for s in fi.readlines(): 
		fo.write(s.replace(search_for, replace_with))
	fi.close() 
	fo.close() 
	try: # remove old backup file, if any 
		os.remove(back)
	except os.error: 
		pass #rename original to backup...
	os.rename(file,back) # ...and temporary to original 
	os.rename(temp,file) ## try it out!

file = "samples/sample.txt"
replace(file, "hello", "tjena")
#replace(file, "tjena", "hello")




'''
处理目录
'''
# 使用 os 列出目录下的文件
# listdir 函数返回给定目录中所有文件名(包括目录名)组成的列表
import os
for file in os.listdir("samples"):
	print(file)


# 使用 os 模块改变当前工作目录
# getcwd 和 chdir 函数分别用于获得和改变当前工作目录
import os 
# where are we?
print("1", os.getcwd())
# go down
os.chdir("samples")
print("2", os.getcwd())
# go back up
os.chdir(os.pardir)
print("3", os.getcwd())



# 使用 os 模块创建/删除多个目录级
# makedirs 和 removedirs 函数用于创建或删除目录层
'''
import os
os.makedirs("test/multiple/levels")
fp = open("test/multiple/levels/file", "w")
fp.write("inspector praline")
fp.close()
os.remove("test/multiple/levels/file")
'''


# 使用 os 模块创建/删除目录
# removedirs 函数会删除所给路径中最后一个目录下所有的空目录. 
# 而 mkdir和 rmdir 函数只能处理单个目录级.
import os
os.mkdir("test")
os.rmdir("test")
#os.rmdir("samples")   # 只能删除非空文件夹


'''
# [注]如果需要删除非空目录, 你可以使用 shutil 模块中的 rmtree 函数.
import shutil
shutil.rmtree("aaa")
'''







'''
处理文件属性
'''
'''
stat 函数可以用来获取一个存在文件的信息
它返回一个类元组对象(stat_result 对象, 包含 10 个元素)：
st_mode (权限模式)
st_ino (inode number)
st_dev (device)
st_nlink (number of hardlinks)
st_uid (所有者用户 ID)
st_gid (所有者所在组 ID )
st_size (文件大小, 字节)
st_atime (最近一次访问时间)
st_mtime (最近修改时间)
st_ctime (平台相关; Unix 下的最近一次元数据/metadata 修改时间, 或者Windows 下的创建时间) 
'''
import os
import time
file = "samples/sample.jpg"
def dump(st):
	mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
	print("- size:", size, "bytes")
	print("- owner:", uid, gid)
	print("- created:", time.ctime(ctime))
	print("- last accessed:", time.ctime(atime))
	print("- last modified:", time.ctime(mtime))
	print("- mode:", oct(mode))
	print("- inode/dev:", ino, dev)

st = os.stat(file)
print("stat--",file, dump(st),'\n')
fp = open(file)
st = os.fstat(fp.fileno())
print("fstat--",file,dump(st),'\n')



# 使用 os 模块修改文件的权限和时间戳
# 可以使用 chmod 和 utime 函数修改文件的权限模式和时间属性

import os
import stat, time
infile = "samples/sample.jpg"
outfile = "samples/out.jpg"
# copy contents
fi = open(infile, "rb")
fo = open(outfile, "wb")
while 1:
	s = fi.read(10000)
	if not s:
		break 
	fo.write(s)
fi.close() 
fo.close()
# copy mode and timestamp
st = os.stat(infile) 
os.chmod(outfile, stat.S_IMODE(st[stat.ST_MODE]))
os.utime(outfile, (st[stat.ST_ATIME], st[stat.ST_MTIME]))
print("original"," =>" )
print("mode",oct(stat.S_IMODE(st[stat.ST_MODE])))
print("atime",time.ctime(st[stat.ST_ATIME]))
print("mtime", time.ctime(st[stat.ST_MTIME]) )
print("copy"," =>" )
st=os.stat(outfile)
print("mode",oct(stat.S_IMODE(st[stat.ST_MODE])))
print("atime", time.ctime(st[stat.ST_ATIME]) )
print("mtime", time.ctime(st[stat.ST_MTIME]))



'''
处理进程
'''

# 使用 os 执行操作系统命令
# system 函数在当前进程下执行一个新命令, 并等待它完成
import os
print(os.name)
if os.name == 'nt':  # 代表Windows
	command = "dir"
else:
	command = "ls -l"
os.system(command)



# 使用 os 模块启动新进程
# exec 函数会使用新进程替换当前进程(或者说是"转到进程").
import os
import sys
program = "python"
arguments = ["hello.py"]
#print(os.execvp(program,(program,) + tuple(arguments)))
print("goodbye")




# 使用 os 模块调用其他程序 (Unix)
# 在 Unix 环境下, 你可以通过组合使用 exec , fork 以及 wait 函数来从当前程序调用另一个程序
# fork 函数复制当前进程, wait函数会等待一个子进程执行结束.
'''
import os
import sys
def run(program, *args):
	pid = os.fork()
	if not pid:
		os.execvp(program, (program,) + args)
	return os.wait()[0]
run("python", "hello.py")
print("goodbye")
'''





# 使用 os 模块调用其他程序 (Windows)
# fork 和 wait 函数在 Windows 上是不可用的, 但是你可以使用 spawn 函数
import os
def run(program, *args):
	for path in str.split(os.environ["PATH"],os.pathsep):
		file = os.path.join(path,program) + ".exe"
		try:
			return os.spawnv(os.P_WAIT,file,(file,)+args)
		except os.error:
			pass
	raise(os.error,"connot find executable")
run("python","hello.py")
print('goodbye-使用 os 模块调用其他程序 (Windows)')




# 使用 os 模块在后台执行程序 (Windows)
# spawn 函数还可用于在后台运行一个程序.
# 给 run 函数添加了一个可选的 mode 参数:
# 当设置为 os.P_NOWAIT 时, 这个脚本不会等待子程序结束；默认值 os.P_WAIT 时 spawn 会等待子进程结束.
import os
def run(program,*args,**kw):
	mode = kw.get('mode',os.P_WAIT)
	for path in str.split(os.environ["PATH"],os.pathsep):
		file = os.path.join(path,program) + ".exe"
		try:
			return os.spawnv(mode,file,(file,)+args)
		except os.error:
			pass
	raise(os.error,"connot find executable")
run('python','hello.py',mode=os.P_NOWAIT)
print('goodbye-使用 os 模块在后台执行程序 (Windows)')




# 使用 spawn 或 fork/exec 调用其他程序
import os
import string
if os.name in ("nt", "dos"):
	exefile = ".exe"
else:
	exefile = ""
def spawn(program, *args):
	try:
		# possible 2.0 shortcut!
		return os.spawnvp(program, (program,) + args)
	except AttributeError:
		pass
	try:
		spawnv = os.spawnv 
	except AttributeError: # assume it's unix
		pid = os.fork() 
		if not pid: 
			os.execvp(program,(program,) + args) 
			return os.wait()[0]
		else: # got spawnv but no spawnp:golook for anexecutable 
			pass
	for path in str.split(os.environ["PATH"],os.pathsep):
		file = os.path.join(path, program) + exefile 
		try: 
			return spawnv(os.P_WAIT, file,(file,)+ args) 
		except os.error: 
			pass 
	raise(IOError, "cannot find executable") # # try it out!
spawn("python", "hello.py")
print("goodbye-使用 spawn 或 fork/exec 调用其他程序") 






'''
处理守护进程(Daemon Processes)
Unix 系统中, 你可以使用 fork 函数把当前进程转入后台(一个"守护者/daemon"). 
一般来说, 你需要派生(fork off)一个当前进程的副本, 然后终止原进程
'''
# 使用 os 模块终止当前进程
import os
import sys
try:
	sys.exit(1)
except SystemExit as value:
	print('1~~caught exit(%s)' % value)
try:
	os._exit(2)
except SystemExit as value:
	print('2~~caught exit(%s)' % value)
print('bye !')









