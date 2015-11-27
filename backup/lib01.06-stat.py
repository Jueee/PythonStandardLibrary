'''
stat 模块
'''

import stat
import os,time

st = os.stat('samples/sample.txt')
print('mode','=>',oct(stat.S_IMODE(st[stat.ST_MODE])))

print('type','=>',end='')
if stat.S_ISDIR(st[stat.ST_MODE]):#判断是否路径
	print('DIRECTORY',end='')
if stat.S_ISREG(st[stat.ST_MODE]):#判断是否一般文件
	print('REGULAR',end='')
if stat.S_ISLNK(st[stat.ST_MODE]):#判断是否链接文件
	print('LINK',end='')
print('')

print('size','=>',st[stat.ST_SIZE])  # 字节

print('last accessed','=>',time.ctime(st[stat.ST_ATIME]))  # 访问时间
print('last modified','=>',time.ctime(st[stat.ST_MTIME]))  # 修改时间
print('inode changed','=>',time.ctime(st[stat.ST_CTIME]))  # 创建时间