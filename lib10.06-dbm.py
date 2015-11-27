'''
dbm 模块
(可选) dbm 模块提供了一个到 dbm 数据库驱动的接口(在许多 Unix 平台上都
可用).
'''
import dbm

db = dbm.open('dbm', 'c')
db["first"] = "bruce"
db["second"] = "bruce"
db["third"] = "bruce"
db["fourth"] = "bruce"
db["fifth"] = "michael"
db["fifth"] = "bruce" # overwrite
db.close()

db = dbm.open('dbm', 'r')
for key in db.keys():
	print(key, db[key])

'''
b'fifth' b'bruce'
b'second' b'bruce'
b'first' b'bruce'
b'third' b'bruce'
b'fourth' b'bruce'
'''