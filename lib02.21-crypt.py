'''
crypt 模块

(可选, 只用于 Unix) crypt 模块实现了单向的 DES 加密, Unix 系统使用这个
加密算法来储存密码, 这个模块真正也就只在检查这样的密码时有用.
'''

'''
# 使用 crypt 模块
# 展示了如何使用 crypt.crypt 来加密一个密码, 将密码和  salt组合起来然后传递给函数, 这里的  salt 包含两位随机字符.
# 现在你可以扔掉原密码而只保存加密后的字符串了.
import crypt
import random
def getsalt(chars = string.letters + string.digits):
	# generate a random 2-character 'salt'
	# 生成随机的 2 字符 'salt'
	return random.choice(chars) + random.choice(chars)
print(crypt.crypt("bananas", getsalt()))
'''


'''
# 使用 crypt 模块身份验证
import pwd, crypt
def login(user, password):
	"Check if user would be able to log in using password"
	try:
		pw1 = pwd.getpwnam(user)[1]
		pw2 = crypt.crypt(password, pw1[:2])
		return pw1 == pw2
	except KeyError:
		return 0 # no such user

user = raw_input("username:")
password = raw_input("password:")

if login(user, password):
	print("welcome", user)
else:
	print("login failed")
'''