'''
msvcrt 模块

(只用于 Windows/DOS ) msvcrt 模块用于访问 Microsoft Visual C/C++
Runtime Library (MSVCRT) 中函数的方法.
'''

'''
# 使用 msvcrt 模块获得按键值
import msvcrt

print("press 'escape' to quit...")

while 1:
	char = msvcrt.getch()
	if char == chr(27):
		break
	print(char, end = '')
	if char == chr(13):
		print()
'''




# 使用 msvcrt 模块接受键盘输入
import msvcrt
import time

print('press SPACE to enter the serial number...')

while not msvcrt.kbhit() or msvcrt.getch != '':
	print('.', end = '')
	time.sleep(0.1)
print()	

# 清除键盘缓冲区
while msvcrt.kbhit():
	msvcrt.getch()

serial = input('enter your serial number:')

print('serial number is', serial)