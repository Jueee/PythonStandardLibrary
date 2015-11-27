'''
array 模块

array 模块实现了一个有效的阵列储存类型. 
阵列和列表类似, 但其中所有的项目必须为相同的类型. 该类型在阵列创建时指定.
'''
# 使用 array 模块将数列转换为字符串
# 创建了一个  array 对象, 然后使用 tostring 方法将内部缓冲区( internal buffer )复制到字符串.
import array

a = array.array("B", range(16)) # unsigned char
b = array.array("h", range(16)) # signed short

print(a)
print(repr(a.tostring()))
print(b)
print(repr(b.tostring()))






# 作为普通序列操作阵列
# array 对象可以作为一个普通列表对待. 不过, 不能连接两个不同类型的阵列.
import array

a = array.array('B', [1, 2, 3])
a.append(4)

a = a + a
a = a[2:-2]

print(a)
print(repr(a.tostring()))
for i in a:
	print(i, end = '')
print('')






# 使用阵列将字符串转换为整数列表
# 用于转换原始二进制数据到整数序列(或浮点数数列, 具体情况决定)的方法
import array

# 必须加“b”，否则会报错：TypeError: an integer is required (got type str)
a = array.array('i', b'fish license')   # signed integer

print(a)
print(repr(a.tostring()))
print(a.tolist())







# 使用 array 模块判断平台字节序
# 使用该模块判断当前平台的字节序( endianess ) .
import array

def little_endian():
	print(array.array('i',[1]).tostring()[0],type(array.array('i',[1]).tostring()[0]),type(str(array.array('i',[1]).tostring()[0])))
	return ord(str(array.array('i',[1]).tostring()[0]))

if little_endian():
	print('little-endian platform(intel, alpha)')
else:
	print('big-endian platform(motorola, sparc)')

'''
1 <class 'int'> <class 'str'>
little-endian platform(intel, alpha)
'''






# 使用 sys.byteorder 属性判断平台字节序
# sys.byteorder 属性, 可以更简单地判断字节序 (属性值为 "little " 或 "big " )
import sys

if sys.byteorder == 'little':
	print('little-endian platform(intel, alpha)')
else:
	print('big-endian platform(motorola, sparc)')





