'''
_winreg 模块

(只用于 Windows , 2.0 中新增) _winreg 模块提供了访问 Windows 注册表数
据库的一个基本接口. 
'''

import winreg

explorer = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\CurrentVersion\\Explorer')
print(explorer)

# 列出该注册表键下的所有值
try:
	i = 0
	while 1:
		name, value, type = winreg.EnumValue(explorer, i)
		print('->', name, '->', value, '->', type)
		i += 1
except WindowsError:
	print()

value, type = winreg.QueryValueEx(explorer, 'Browse For Folder Height')
print()
print('user is',value)

'''
<PyHKEY:0x00000194>
-> ExplorerStartupTraceRecorded -> 1 -> 4
-> ShellState -> b'$\x00\x00\x00:(\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00"\x00\x00\x00' -> 3
-> CleanShutdown -> 0 -> 4
-> link -> b'\x00\x00\x00\x00' -> 3
-> Browse For Folder Width -> 318 -> 4
-> Browse For Folder Height -> 288 -> 4
-> DesktopProcess -> 1 -> 4


user is 288
[Finished in 0.2s]
'''