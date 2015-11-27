'''
anydbm 模块

anydbm 模块为简单数据库驱动提供了统一标准的接口.

当第一次被导入的时候, anydbm 模块会自动寻找一个合适的数据库驱动, 按照
dbhash , gdbm , dbm , 或 dumbdbm 的顺序尝试. 

如果没有找到任何模块, 它将引发一个  ImportError 异常.


open 函数用于打开或创建一个数据库(使用导入时找到的数据库驱动)

dbm#

所有的dbm克隆(dbm clone)现在在单独的一个包里，即dbm。如果你需要其中某个特定的变体，比如gnu dbm，你可以导入dbm包中合适的模块。

Notes	Python 2	Python 3
import dbm			import dbm.ndbm
import gdbm			import dbm.gnu
import dbhash		import dbm.bsd
import dumbdbm		import dbm.dumb
import anydbm   	import dbm
import whichdb  	import dbm
'''
# 使用 anydbm 模块
import dbm

db = dbm.open('database', 'c')
print(db)
db['1'] = 'one'
db['2'] = 'two'
db['3'] = 'three'
db.close()

db = dbm.open('database', 'r')
for key in db.keys():
	print(key, db[key])
	
'''
<dbm.dumb._Database object at 0x02C05EF0>
b'1' b'one'
b'2' b'two'
b'3' b'three'
'''