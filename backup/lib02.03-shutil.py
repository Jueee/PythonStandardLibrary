'''
shutil 模块

shutil 实用模块包含了一些用于复制文件和文件夹的函数.
'''

# 使用 shutil 复制文件
# copy 函数使用和 Unix 下 cp 命令基本相同的方式复制一个文件.
import shutil
import os 

for file in os.listdir('.'):
	if os.path.splitext(file)[1] == '.py':
		print(file)
		shutil.copy(file,os.path.join("backup", file))



# 使用 shutil 模块复制/删除目录树
# copytree 函数用于复制整个目录树 (与 cp -r 相同), 
# rmtree 函数用于删除整个目录树 (与 rm -r ).

import shutil
import os

SOURCE = 'samples'
BACKUP = 'samples-bak'

# create a backup directory
#shutil.copytree(SOURCE, BACKUP)
print(os.listdir(BACKUP))

# remove it
shutil.rmtree(BACKUP)
print(os.listdir(BACKUP))
