'''
quopri 模块

quopri 模块基于 MIME 标准实现了引用的可打印编码( quoted printable encoding ).

这样的编码可以将不包含或只包含一部分 U.S. ASCII 文本的信息, 例如大多欧洲语言, 中文, 转换为只包含 U.S. ASCII 的信息. 
在一些老式的 mail 代理中你会发现这很有用, 因为它们一般不支持特殊. 
'''
import quopri
import io

def encodestring(instring, tabs = 0):
	outfile = io.StringIO()
	print(io.StringIO(instring),type(io.StringIO(instring)))
	print(outfile,type(outfile))
	quopri.encode(io.StringIO(instring), outfile, tabs)
	return outfile.getvalue()

def decodestring(instring):
	outfile = io.StringIO()
	quopri.decode(io.StringIO(instring), outfile)
	return outfile.getvalue()

MESSAGE = '?i?a?e?!'

encode_message = encodestring(MESSAGE)
decode_message = decodestring(encode_message)

print('original:',MESSAGE)
print("encoded message:", repr(encoded_message))
print("decoded message:", decoded_message)







