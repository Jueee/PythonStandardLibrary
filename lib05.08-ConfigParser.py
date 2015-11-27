'''
ConfigParser 模块

ConfigParser 模块用于读取配置文件.

配置文件的格式与 Windows INI 文件类似, 可以包含一个或多个区域( section ), 每个区域可以有多个配置条目.

python 3.3 的 ConfigParser 改成 configparser 了
'''
# 使用 ConfigParser 模块
import configparser

config = configparser.ConfigParser()
config.read('samples/sample.ini')

print()
print(str.upper(config.get('book', 'title')))
print('by', config.get('book', 'author'), end = '')
print('(' + config.get('book', 'email') + ')')
print()
print(config.get('ematter', 'pages'), 'pages')
print()

for section in config.sections():
	print(section)
	for option in config.options(section):
		print(' ', option, '=', config.get(section, option))





print('------------')



# 使用 ConfigParser 模块写入配置数据
import configparser
import sys

config = configparser.ConfigParser()
config.add_section('book')
config.set('book', 'title', 'the Python Stardard library')
config.set('book', 'author', 'fredrik lundh')

config.add_section('ematter')
config.set('ematter', 'pages', '257')

config.write(sys.stdout)