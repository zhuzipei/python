import os.path


input =  open(r"D:\works\IOtest\test1.txt",'r')#encoding="gbk",errors="ignore"
#r:read w:write a:append rd:read binary wb:write binary
input.read(size)
input.readline()#末尾返回''
input.readlines()#list
input.write()#覆盖原文件
input.close()
os.path.isfile()#boolean

with open(r"D:\works\IOtest\test1.txt",'r') as f:
    c