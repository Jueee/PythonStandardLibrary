'''
base64 模块

base64 编码体系用于将任意二进制数据转换为纯文本. 

它将一个 3 字节的二进制字节组转换为 4 个文本字符组储存, 而且规定只允许以下集合中的字符出现:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789+/

另外, = 用于填充数据流的末尾.
'''
'''
# 使用 base64 模块编码文件
import base64

MESSAGE = "life of brian"

file = open("out.txt", "w")
file.write(MESSAGE)
file.close()
print(open("out.txt").read())
base64.encode(open("out.txt"), open("out.b64", "w"))
base64.decode(open("out.b64"), open("out.txt", "w"))
print("original:", repr(MESSAGE))
print("encoded message:", repr(open("out.b64").read()))
print("decoded message:", repr(open("out.txt").read()))
'''





# 使用 base64 模块编码字符串
# 使用 encodestring 和 decodestring 函数在字符串间转换.
# 它们是 encode 和 decode 函数的顶层封装.
# 使用 StringIO 对象处理输入和输出.
import base64

MESSAGE = b"life of brian"
data = base64.encodestring(MESSAGE)
original_data = base64.decodestring(data)
print("original:", repr(MESSAGE))
print("encoded data:", repr(data))
print("decoded data:", repr(original_data))








# 使用 base64 模块做基本验证
# 将用户名和密码转换为 HTTP 基本身份验证字符串.
import base64

def getbasic(user, password):
	# basic authentication (according to HTTP)
	return base64.encodestring(user + b':' + password)

print(getbasic(b'Aladdin', b'open sesame'))








# 使用 base64 为 Tkinter 封装 GIF 格式
# 一个实用小工具, 它可以把 GIF 格式转换为Python 脚本, 便于使用 Tkinter 库.
import base64, sys
import builtins

'''
print(sys.argv[1:])
if not sys.argv[1:]:
	print('Usage: gif2tk.py giffile > pyfile')
	sys.exit(1)

# data = open(sys.argv[1], 'rb').read()
'''
file = builtins.open('samples/sample.gif', 'rb')
print("file.read(5):",file.read(5))
if file.read(5) not in("GIF87", "GIF89"): 
	print("not a GIF file")

print('# generated from', sys.argv[0], 'by gif2tk.py')
print('')
print('from Tkinter import PhotoImage')
print('')
print('image = PhotoImage(data="""')
print(base64.encodestring(data),)
print('""")')



