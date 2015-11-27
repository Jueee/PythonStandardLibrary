'''
sha 模块

sha 模块提供了计算信息摘要(密文)的另种方法. 
它与 md5 模块类似, 但生成的是 160 位签名.

Python3 移除了 audiodev, Bastion, bsddb185, exceptions, linuxaudiodev, md5, MimeWriter, mimify, popen2,  
rexec, sets, sha, stringold, strop, sunaudiodev, timing和xmllib模块
'''
from  hashlib import sha1

hash = sha1()
print(hash)
hash.update(b'spam, spam, and eggs')
print(hash.digest())
print(hash.hexdigest())


