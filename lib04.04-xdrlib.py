'''
xdrlib 模块

xdrlib 模块用于在 Python 数据类型和 Sun 的 external data representation (XDR) 间相互转化
'''
import xdrlib

# create a packer and add some data to it
p = xdrlib.Packer()
p.pack_uint(1)
p.pack_string(b'spam')

data = p.get_buffer()
print('packer:', repr(data))

# create an unpacker and use it to decode the data
u = xdrlib.Unpacker(data)
print('unpacked:', u.unpack_uint(), u.unpack_string())







# 使用 xdrlib 模块发送 RPC 调用包
# Sun 在 remote procedure call (RPC) 协议中使用了 XDR 格式.
import xdrlib

# some constants (see the RPC specs for details)
RPC_CALL = 1
RPC_VERSION = 2

MY_PROGRAM_ID = 1234 
MY_VERSION_ID = 1000
MY_TIME_PROCEDURE_ID = 9999

AUTH_NULL = 0

transaction = 1

p = xdrlib.Packer()

# send a Sun RPC call package
p.pack_uint(transaction)
p.pack_enum(RPC_CALL)
p.pack_uint(RPC_VERSION)
p.pack_uint(MY_PROGRAM_ID)
p.pack_uint(MY_VERSION_ID)
p.pack_uint(MY_TIME_PROCEDURE_ID)
p.pack_enum(AUTH_NULL)
p.pack_uint(0)
p.pack_enum(AUTH_NULL)
p.pack_uint(0)

print(repr(p.get_buffer()))