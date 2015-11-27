'''
shelve 模块

shelve 模块使用数据库驱动实现了字典对象的持久保存. 
shelve 对象使用字符串作为键, 但值可以是任意类型, 所有可以被 pickle 模块处理的对象都可以作为它的值. 
'''
import shelve

db = shelve.open('database', 'c')
db['one'] = 1
db['two'] = 2
db['three'] = 3
db.close()

db = shelve.open('database', 'r')
print(db)
print(dir(db))
print(db.keys(), type(db.keys()))
print(list(db.keys()))
print(db.items(), type(db.items()))
print(db.values(), type(db.values()))
for key in db.keys():
	print(key)






# 使用 shelve 模块处理给定数据库
import shelve
import gdbm