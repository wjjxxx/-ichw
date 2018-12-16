# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:00:53 2018

@author: HP
"""

import turtle
import sys
import random
sys.getrecursionlimit=100000

def a_wall(m,n):
    #建一个表示m*n墙的列表，每个单元都用坐标表示
    list=[]
    for y in range(n):
        for x in range(m):
            list.append([x,y])
    return list

def brick(z,x,y):
    #以墙上的坐标为左下角，建立一个表现一块x*y砖块的列表
    a=a_wall(x,y)
    for b in a:
        b[0]+=z[0]
        b[1]+=z[1]
    return a
    
def shanjian(wall,x,y):
    #若某砖在墙内，则返回该砖的表达式，并从墙列表中删去该砖包含的坐标。
    a=brick(wall[0],x,y)
    for b in a:
        if b in wall:
            continue
        else:
            break
    else:
        for b in a:
            wall.remove(b)
        return a
    
def shibie(wall,x,y):
    #返回所有密铺方式，但会有一些没有完全密铺的，未完全密铺的用‘Note’做标记
    if x==y:
        wallcopy=wall.copy()
        if len(wallcopy)==0:
          return [[]]
        else:
            b=shanjian(wallcopy,x,y)
            a=shibie(wallcopy,x,y)
            for o in a:
                o.append(b)
            return [o]
    else:
        a=wall.copy()
        b=wall.copy()
        if len(wall)==0:
            return [[]]
        if len(a)>0 and len(b)>0:
            c=shanjian(a,x,y)
            d=shanjian(b,y,x)
            if c!=None and d!=None:
                e=shibie(a,x,y)
                for p in e:
                    p.append(c) 
                f=shibie(b,y,x)
                for q in f:
                    q.append(d)
                return e+f
            if c!=None and d==None:
                e=shibie(a,x,y)
                for p in e:
                    p.append(c)
                return e
            if c==None and d!=None:
                f=shibie(b,x,y)
                for q in f:
                    q.append(d)
                return f
            if c==None and d==None:
                return[['Note']]

def final_methods(wall,x,y):
    #对shibie得到的粗列表筛选出未标记的
    new_list=[]
    for i in shibie(wall,x,y):
        if 'Note' not in str(i):
            new_list.append(i)
    return new_list

def output(m,n,x,y):
    #把密铺方式中基本单位的坐标形式变成整数格式，做符合要求的形式输出。
    wall=a_wall(m,n)
    methods=final_methods(wall,x,y).copy()
    new_methods=[]
    for i in methods:
        new_method=[]
        for brick in i:
            new_brick=[]
            for a in brick:
                number=m*a[1]+a[0]
                new_brick.append(number)
            new_method.append(tuple(new_brick))
        new_methods.append(new_method)
    for x in new_methods:
        print(x)

def draw_square(a,b,fillcolor):
    #画边长为b，涂色为fillcolor的正方形。
    turtle.tracer(False)
    lsx=turtle.Turtle()
    lsx.color('black',fillcolor)
    lsx.up()
    lsx.goto(a[0],a[1])
    lsx.down()
    lsx.begin_fill()
    for x in range(4):
        lsx.forward(b)
        lsx.left(90)
    lsx.end_fill()
    lsx.hideturtle()
    turtle.tracer(True)
    
def draw_wall(m,n):
    #画网格
    length=600/max(m,n)
    for element in a_wall(m,n):
        coordinate=(length*(element[0]-m/2),length*(element[1]-n/2))
        draw_square(coordinate,length,'white')
    return length

def draw_a_brick(brick,fillcolor,m,n):
    #以构造砖的坐标形式为自变量来绘制以fillcolor为颜色的砖块
    length=600/max(m,n)
    for i in brick:
        b=(length*(i[0]-m/2),length*(i[1]-n/2))
        draw_square(b,length,fillcolor)

def draw_a_method(method,m,n,x,y):
    #用不同颜色的砖块，画出一种密铺方法
    colorlist=[]
    for p in range(0,65536*256-1,(65536*256)//((m*n)//(x*y)+1)):
        colorlist.append('#'+'{:0>6s}'.format('{:X}'.format(p)))
    for brick in method:
        draw_a_brick(brick,colorlist[method.index(brick)%len(colorlist)],m,n)
        
def major(m,n,x,y):
    #打印出密铺结果，将其中任意一个在turtle上可视化。
    wall=a_wall(m,n)
    draw_wall(m,n)
    methods=final_methods(wall,x,y)
    draw_a_method(methods[random.randrange(len(methods))],m,n,x,y)
    output(m,n,x,y)

def main():
    major(int(input('墙的长度:',)),\
          int(input('墙的宽度:',)),\
          int(input('砖的长度:',)),\
          int(input('砖的宽度:',)))

if __name__ == '__main__':
    main()
