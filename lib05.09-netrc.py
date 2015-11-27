'''
netrc 模块

netrc 模块可以用来解析  .netrc 配置文件

该文件用于在用户的 home 目录储存 FTP 用户名和密码. 
(别忘记设置这个文件的属性为: "chmod 0600 ~/.netrc," 这样只有当前用户能访问).
'''
# 使用 netrc 模块
import netrc

help(netrc)
info = netrc.netrc('samples/sample.netrc')

login, account, password = info.authenticators('secret.fbi')

print("login", "=>", repr(login))
print("account", "=>", repr(account))
print("password", "=>", repr(password))




