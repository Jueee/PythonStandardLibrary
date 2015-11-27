'''
zipfile 模块

zipfile 模块可以用来读写 ZIP 格式.
'''

# 使用 zipfile 模块列出 ZIP 文档中的文件
# 使用 namelist 和 infolist 方法可以列出压缩档的内容, 前者返回由文件名组成的列表, 后者返回由  ZipInfo 实例组成的列表.
import zipfile

file = zipfile.ZipFile('samples/sample.zip', 'r')

print(file.namelist())
for name in file.namelist():
	print(name, end = '')
print()

for info in file.infolist():
	print(info.filename, info.date_time, info.file_size)


print('-----------')



# 从 ZIP 文件中读取数据
# 调用 read 方法就可以从 ZIP 文档中读取数据. 它接受一个文件名作为参数, 返回字符串.
import zipfile

file = zipfile.ZipFile('samples/sample.zip', 'r')

for name in file.namelist():
	data = file.read(name)
	print(name, len(data), data[:100])




print('-----------')






# 使用 zipfile 模块将文件储存在 ZIP 文件里
# 向 ZIP 文件写入数据
# 向压缩档加入文件很简单, 将文件名, 文件在 ZIP 档中的名称传递给 write方法即可.
import zipfile
import glob, os

file = zipfile.ZipFile('test.zip', 'w')

for name in glob.glob('samples/*'):
	# write 方法的第三个可选参数用于控制是否使用压缩. 
	# 默认为 zipfile.ZIP_STORED , 意味着只是将数据储存在档案里而不进行任何压缩. 
	# 如果安装了 zlib 模块, 那么就可以使用 zipfile.ZIP_DEFLATED 进行压缩.
	file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
file.close()

file = zipfile.ZipFile('test.zip', 'r')
for info in file.infolist():
	print(info.filename, info.date_time, info.file_size, info.compress_size)


print('-----------')



# 使用 zipfile 模块在 ZIP 文件中储存字符串
# zipfile 模块也可以向档案中添加字符串. 
# 不过, 这需要一点技巧, 你需要创建一个  ZipInfo 实例, 并正确配置它.
import zipfile
import glob, os, time

file = zipfile.ZipFile('test.zip', 'w')

now = time.localtime(time.time())[:6]
for name in ('life', 'of', 'brian'):
	print(name)
	info = zipfile.ZipInfo(name)
	info.date_time = now
	info.compress_size = zipfile.ZIP_DEFLATED
	file.writestr(info, name * 1000)

file.close()

file = zipfile.ZipFile('test.zip', 'r')
for info in file.infolist():
	print(info.filename, info.date_time, info.file_size, info.compress_size)

















