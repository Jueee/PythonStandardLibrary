'''
popen2 模块

popen2 模块允许你执行外部命令, 并通过流来分别访问它的 stdin 和 stdout( 可能还有 stderr ).

Python 3 移除了 audiodev, Bastion, bsddb185, exceptions, linuxaudiodev, md5, MimeWriter, mimify, popen2,  
rexec, sets, sha, stringold, strop, sunaudiodev, timing和xmllib模块 
'''
# 使用 popen2 模块对字符串排序 Module to Sort Strings
import popen2

fin, fout = popen2.popen2("sort")

fout.write("foo\n")
fout.write("bar\n")
fout.close()

print fin.readline(),
print fin.readline(),

fin.close()
'''
bar
foo
'''









# 使用 popen2 模块控制 gnuchess
import popen2
import string

class Chess:
	"Interface class for chesstool-compatible programs"
	def __init__(self, engine = "gnuchessc"):
		self.fin, self.fout = popen2.popen2(engine)
		s = self.fin.readline()
		if s != "Chess\n":
			raise IOError, "incompatible chess program"
	def move(self, move):
		self.fout.write(move + "\n")
		self.fout.flush()
		my = self.fin.readline()
		if my == "Illegal move":
		raise ValueError, "illegal move"
		his = self.fin.readline()
		return string.split(his)[2]
	def quit(self):
		self.fout.write("quit\n")
		self.fout.flush()



#
# play a few moves
g = Chess()

print g.move("a2a4")
print g.move("b2b3")

g.quit()

'''
b8c6
e7e5
'''