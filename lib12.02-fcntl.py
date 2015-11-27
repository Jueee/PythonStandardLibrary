'''
fcntl 模块

(只用于 Unix) fcntl 模块为 Unix 上的 ioctl 和 fcntl 函数提供了一个接口.
它们用于文件句柄和 I/O 设备句柄的 "out of band" 操作, 包括读取扩展属性,
控制阻塞. 更改终端行为等等. (out of band management: 指使用分离的渠道
进行设备管理. 这使系统管理员能在机器关机的时候对服务器, 网络进行监视
和管理. 

该模块同时提供了 Unix 文件锁定机制的接口. 
'''
import fcntl