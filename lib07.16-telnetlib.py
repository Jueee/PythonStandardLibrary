'''
telnetlib 模块

telnetlib 模块提供了一个 telnet 客户端实现.
'''
# 使用 telnetlib 模块登陆到远程服务器
import telnetlib
import sys

HOST = "192.168.50.74"

USER = "hs\administrator"
PASSWORD = "hundsun@1"

telnet = telnetlib.Telnet(HOST)

telnet.read_until('login:')
telnet.write(USER + '\n')

telnet.read_until('Password:')
telnet.write(PASSWORD + '\n')

telnet.write('1s librarybook\n')
telnet.write('exit\n')

print(telnet.read_all())