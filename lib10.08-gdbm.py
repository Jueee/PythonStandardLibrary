'''
gdbm 模块
(可选) gdbm 模块提供了到 GNU dbm 数据驱动的接口
'''

import dbm.gnu

db = dbm.gnu.open("gdbm", "c")
db["1"] = "call"
db["2"] = "the"
db["3"] = "next"
db["4"] = "defendant"
db.close()

db = dbm.gnu.open("gdbm", "r")
keys = db.keys()
keys.sort()
for key in keys:
	print(db[key], end = '')