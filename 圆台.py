from tkinter import *
import time
import math
import types

PI=math.pi

def biaomianji(r1, r2, h):
    if r1 > r2:
        r1, r2=r2, r1
    elif r1 == r2:
        if r1 != 0:
            yuanzhu=True
        else:
            return input('数据有误，请重新输入')
    l1=(r1**2+(r1*h/(r2-r1))**2)**0.5
    l2=l1*r2/r1
    result=format(r1**2+r2**2+2*PI*(l1-l2),'.2f')
    return result

def tiji(r1,r2,h):
    if r1 > r2:
        r1,r2=r2,r1
    elif r1 == r2:
        if r1 != 0:
            yuanzhu=True
        else:
            return input('数据有误，请重新输入')
    result=format((r1**2+r2**2+r1*r2)*h*PI/3,'.2f')
    return result

def natural_number_check(n):
    try:
       a=float(n)
    except:
        return natural_number_check(input('数据有误，请重新输入'))
    if a < 0:
        return natural_number_check(input('数据有误，请重新输入'))
    else:
        return True

def data_capture():
    r1=input('请输入圆台的底面半径：')
    r2=input('请输入圆台的底面半径：')
    h=input('请输入圆台的高：')
    if natural_number_check(r1) is True:
        r1=eval(r1)
    if natural_number_check(r2) is True:
        r2=eval(r2)
    if natural_number_check(h) is True:
        h=eval(h)
    return r1,r2,h

def input_check(a):
    if a.isdigit() is True and a[0] != '0':
        if eval(a) == 1:
            print('您将获得该圆台的体积')
            print('该几何体的体积为：',tiji(data_capture()))
        elif eval(a) == 2:
            print('您将获得该圆台的表面积')
            print('该几何体的体积为：',biaomianji(data_capture()))
        else:
            print('输入数据有误')
    else:
        return input_check(input('数据有误，请重新输入'))

window=Tk()
window.title('CA')
label=Label(window,text='你可以使用本程序计算圆台、圆柱与圆锥的体积与表面积。计算体积请输入1，计算表面积请输入2').pack()

button1=Button(window,text='体积',command=).pack()
button2=Button(window,text='面积',command=).pack()
entry1=
entry2=
entry3=
window.mainloop()
a=input('你可以使用本程序计算圆台、圆柱与圆锥的体积与表面积。计算体积请输入1，计算表面积请输入2')
input_check(a)
