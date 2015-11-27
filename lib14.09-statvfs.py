'''
statvfs 模块

statvfs 模块包含一些与 os.statvfs (可选)函数配合使用的常量和函数, 该
函数会返回文件系统的相关信息.
'''
import os

st = os.statvfs(".")
print("preferred block size", "=>", st[statvfs.F_BSIZE])
print("fundamental block size", "=>", st[statvfs.F_FRSIZE])
print("total blocks", "=>", st[statvfs.F_BLOCKS])
print("total free blocks", "=>", st[statvfs.F_BFREE])
print("available blocks", "=>", st[statvfs.F_BAVAIL])
print("total file nodes", "=>", st[statvfs.F_FILES])
print("total free nodes", "=>", st[statvfs.F_FFREE])
print("available nodes", "=>", st[statvfs.F_FAVAIL])
print("max file name length", "=>", st[statvfs.F_NAMEMAX])