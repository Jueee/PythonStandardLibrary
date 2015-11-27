'''
binascii 模块

binascii 提供了多个编码的支持函数, 包括 base64 , binhex , 以及 uu . 

还可以使用它在二进制数据和十六进制字符串中相互转换.
'''
# 使用 binascii 模块
import binascii

text = b'hello, mrs teal'

data = binascii.b2a_base64(text)
text = binascii.a2b_base64(data)
print(text, '<=>', data)

data = binascii.b2a_uu(text)
text = binascii.a2b_uu(data)
print(text, '<=>', data)

data = binascii.b2a_hqx(text)
text = binascii.a2b_hqx(data)[0]
print(text, '<=>', data)

data = binascii.b2a_hex(text)
text = binascii.a2b_hex(data)
print(text, '<=>', data)


'''
b'hello, mrs teal' <=> b'aGVsbG8sIG1ycyB0ZWFs\n'
b'hello, mrs teal' <=> b'/:&5L;&\\L(&UR<R!T96%L\n'
b'hello, mrs teal' <=> b'D\'9XE\'mX)\'ebFb"dC@&X'
b'hello, mrs teal' <=> b'68656c6c6f2c206d7273207465616c'
'''