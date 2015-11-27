'''
linecache 模块

linecache 模块用于从模块源文件中读取代码. 
它会缓存最近访问的模块 (整个源文件).
'''
import linecache

print(linecache.getline('lib13.13-linecache.py', 5))

'''
它会缓存最近访问的模块 (整个源文件).

[Finished in 0.3s]
'''