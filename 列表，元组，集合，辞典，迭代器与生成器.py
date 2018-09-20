import random


list = ['A',123,True,[1,2,3]]
list.append('D')
list.insert(0,'Z')
list.pop(0)
list.pop(1)
L = len(list)
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):#下标起始位置
    print index, item

t = (1,)#tuple
zipped = zip(a,b)#将可迭代对象打包为元组，zip（zipped*a）为解压

a = [1,2,3]
b = ['a','b','c']
c = a+b
d = a*2
e = a[:2:2]

#print(max(a))
#print(random.shuffle(a))
a.count(1)
#a.extend(b)
a.remove(2)#first only
a.reverse()
a.sort()
#print(a)
stc = '章鱼丸子，水煎肉'.split('，')
#print(stc)
b = a
b.append('as')#a、b同步！
b = a+[]#right
print(a,b)
#列表是可变对象
#默认值只创建一次
def add(x,lst=None):
    if lst == None:
        lst = []

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
'Thomas' in d
d[key]
d.get('Thomas',34)#34为指定不存在返回值
d.pop(key)
d.keys()
d.values()
d.items()
d.clear()
d.popitem()
#本质哈希，set与dict的key不能为可变对象，包括含有dict,set,list的tuple

s=set([1,2,3])
s.remove()
s.add()
s1&s2#交集
s1|s2#并集
s1-s2
s1^s2#交集的补集

list()
tuple()
set()

[x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ']
d={'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,'=',v)

g=(x*x for x in range(10))#可迭代
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b#生成器关键词?
        a, b = b, a + b
        n = n + 1
    return 'done'