'''
ftplib 模块

ftplib 模块包含了一个 File Transfer Protocol (FTP , 文件传输协议)客户端的实现.

'''
import ftplib

ftp = ftplib.FTP('www.zhihu.com')
ftp.login('921550356@qq.com','123yongqiang')
print(ftp.dir())

ftp.quit()





