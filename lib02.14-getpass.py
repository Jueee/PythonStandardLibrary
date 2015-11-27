'''
getpass 模块

getpass 模块提供了平台无关的在命令行下输入密码的方法.

getpass(prompt) 会显示提示字符串, 关闭键盘的屏幕反馈, 然后读取密码.
如果提示参数省略, 那么它将打印出 "Password: ".

getuser() 获得当前用户名, 如果可能的话.
'''

import getpass

user = getpass.getuser()
pwd = getpass.getpass('enter Password for user %s:' % user)

print(user, pwd)


# 加一个输入语句，使运行后命令窗口不自动关闭
input("Prease <enter>")