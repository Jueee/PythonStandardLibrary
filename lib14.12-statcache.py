'''
statcache 模块

statcache 模块提供了访问文件相关信息的相关函数. 

它是 os.stat 的扩展模块, 而且它会缓存收集到的信息. 

2.2 后该模块被废弃, 请使用 os.stat() 函数代替, 原因很简单, 它导致了更
复杂的缓存管理, 反而降低了性能.
'''
import statcache