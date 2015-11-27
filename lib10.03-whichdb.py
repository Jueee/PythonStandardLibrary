'''
whichdb 模块

whichdb 模块可以判断给定数据库文件的格式

Notes	Python 2	Python 3
import dbm			import dbm.ndbm
import gdbm			import dbm.gnu
import dbhash		import dbm.bsd
import dumbdbm		import dbm.dumb
import anydbm   	import dbm
import whichdb  	import dbm
'''
import dbm

filename = 'database'
result = dbm.whichdb(filename)
print(result)

if result:
	print('file created by', result)
	handler = __import__(result)
	db = handler.open(filename, 'r')
	print(db.keys())
else:
	if result is None:
		print("cannot read database file", filename)
	else:
		print("cannot identify database file", filename)
	db = None

'''
dbm.dumb
file created by dbm.dumb
[b'2', b'3', b'1']
'''