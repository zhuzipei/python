import math
from functools import *
from tkinter import *
import os.path
# def factorial(n):
#    n=int(n)
#    if n == 0:
#	    return 1
#    else:
#	    return n*factorial(n-1)
# print(factorial(input()))
# t=(1,2,3,('a','b','c'))
# s=(t,4,5)
# print(t)
# print(s)
# print(type(t),type(s))
# a={1,2,3}
# b={a,'c','d'}
# a=[1,2,3]
# b={1,2,3}
# c=(1,2,3)
# d={'a':1,'b':2,'c':3}
# print(1 in a, 1 in b,1 in c,'a' in d,1 in d)
# a=[1,2,3]
# e=a[3%len(a)]
# print(e)
# for i in range(9):
# 	print(i,end=' ')
# print(1)
# print(True)
# def not_empty(s):
#     return s and s.strip()
# print(bool(not_empty('')))#?
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# a=lazy_sum(1,2,3)
# print(a())
# 返回函数不要引用任何循环变量
# def add(x,y):
# 	return x+y
# def a(*args):
# 	def b():
# 		return reduce(add,list(args))
# 	return b
# x=a(1,2,3)
# print(x())
# print(type(x))
# def add1(x):
# 	x += 1
# 	return x
# print(type((map(add1,[x**2 for x in range(1,5)]))))
# a=[]
# b=a+[]
# a+=[1]
# print(a)
# print(b)
# print(23%23)
# def is_odd(n):
#     return 1
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# print(1%2)
# def f():
# 	return 1,2
# print(type(f()))tuple
# if bool(0) and bool(2) is True:
# 	print(1)
# else:
# 	print(0)
# class Dog():

# 	def __ini"\u6B22"t__(self):
# 		pass

# 	def __len__(self):
# 		return 100

# print(len(Dog()))
# print(round(1.45,3))
# print('a\nb\rc')
# print(format('1234567','10s'))
# def main():
#     input =  open(r"D:\works\IOtest\test1.txt",'w')
#     input.write(str([1,2,3]))
#     input.close()
# main()
# def main():
#     if os.path.isfile(r"D:\works\IOtest\test1.txt"):
#         input = open(r"D:\works\IOtest\test1.txt",'r')
#         output = open(r"D:\works\IOtest\test2.txt",'a')
#         for line in input:
#             output.write(line)
# main()
# def main():
# 	return [1,2,3]
# print(main())
def pretreat(str):
    for char in str:
        if not re.match(r'[0-9a-zA-Z\-]',char):
            str = str.replace(char,' ')
    str = str.lower()
    return str
print(pretreat('asb书岁lkj'))