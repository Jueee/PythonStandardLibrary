'''
dumbdbm 模块

dumbdbm 模块是一个简单的数据库实现, 与 dbm 一类相似, 但使用纯 Python实现. 

它使用两个文件: 
一个二进制文件 ( .dat ) 用于储存数据, 一个文本文件 ( .dir ) 用于数据描述.
'''
import dbm.dumb

db = dbm.dumb.open("dumbdbm", "c")
db["first"] = "fear"
db["second"] = "surprise"
db["third"] = "ruthless efficiency"
db["fourth"] = "an almost fanatical devotion to the Pope"
db["fifth"] = "nice red uniforms"
db.close()

db = dbm.dumb.open("dumbdbm", "r")
for key in db.keys():
	print(repr(key), repr(db[key]))

'''
b'fifth' b'nice red uniforms'
b'second' b'surprise'
b'first' b'fear'
b'third' b'ruthless efficiency'
b'fourth' b'an almost fanatical devotion to the Pope'
'''