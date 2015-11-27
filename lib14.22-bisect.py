'''
bisect 模块

bisect 模块用于向排序后的序列插入对象.

insort(sequence, item) 将条目插入到序列中, 并且保证序列的排序. 

序列可以是任意实现了 __getitem__ 和 insert 方法的序列对象.
'''
# 使用 bisect 模块向列表插入条目
import bisect

list = [10, 20, 30]

bisect.insort(list, 25)
bisect.insort(list, 15)

print(list)
'''
[10, 15, 20, 25, 30]
'''




# 使用 bisect 模块获得插入点位置
# bisect(sequence, item) => index 返回条目插入后的索引值, 不对序列做任何修改.
import bisect

list = [10, 20, 30]

print(list)
print(bisect.bisect(list, 25))
print(list)
print(bisect.bisect(list, 15))
print(list)

'''
[10, 20, 30]
2
[10, 20, 30]
1
[10, 20, 30]
'''









