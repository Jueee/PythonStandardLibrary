'''
imghdr 模块

imghdr 模块可识别不同格式的图片文件. 

当前版本可以识别 bmp , gif , jpeg , pbm , pgm , png , ppm , rast (Sun raster), rgb (SGI), tiff , 以及 xbm 图像.

'''
# 使用 imghdr 模块
import imghdr

result = imghdr.what('samples/sample.jpg')
print(result)
if result:
	print('file format', result)
else:
	print('connot identify file')


