'''
struct 模块

struct 模块用于转换二进制字符串和 Python 元组. 
pack 函数接受格式字符串以及额外参数, 根据指定格式将额外参数转换为二进制字符串. 
upack 函数接受一个字符串作为参数, 返回一个元组.
'''
import struct

# native byteorder 
buffer = struct.pack('ihb', 1, 2, 3)
print(repr(buffer))
print(struct.unpack('ihb', buffer))

# data from a sequence, network byteorder
data = [1, 2, 3]
print(tuple(data))
# 原：buffer = struct.pack("ihb", 1, 2, 3)
# 已经不支持了 apply(self.func,self.args) 改为 self.func(*self.args)
buffer = struct.pack('!ihb', *data)
print(buffer)
