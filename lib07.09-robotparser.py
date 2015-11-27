'''
robotparser 模块

 robotparser 模块用来读取 robots.txt 文件
'''
import urllib.robotparser

r = urllib.robotparser.RobotFileParser()
r.set_url('http://www.baidu.com/robots.txt')
r.read()

print(r)

if r.can_fetch('*', '/index.html'):
	print('may fetch the home page')

if r.can_fetch('*', '/tim_ont/index.html'):
	print('may fetch the tim peters archive')