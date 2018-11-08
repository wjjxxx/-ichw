# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:03:49 2018

@author: HP
"""

import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")

tai=turtle.Turtle()
tai.color("orange")
tai.shape("circle")
tai.shapesize(3)

shui=turtle.Turtle()
shui.color("dark blue")
jin=turtle.Turtle()
jin.color("gold")
di=turtle.Turtle()
di.color("blue")
huo=turtle.Turtle()
huo.color("red")
mu=turtle.Turtle()
mu.color("yellow")         
tu=turtle.Turtle()
tu.color("brown")
wei=turtle.Turtle()
wei.color("grey")
wei.speed(0)
wei.up()

tur=[shui,di,huo,mu,tu,jin]
po=[500,1000,480,1700,1900,750]
eo=[10,12,5,13,10,11]

for xingxin in range(6):
        xin=tur[xingxin]
        xin.speed(0)
        xin.hideturtle()
        xin.up()
        xin.shape("circle")
        jiao=0
        p=po[xingxin]
        e=eo[xingxin]
        chang=p/(e-math.cos(jiao))
        a=chang*math.cos(jiao)
        b=chang*math.sin(jiao)
        xin.goto(a,b)
        xin.down()
        xin.showturtle()      

for i in range(1000):
    pjin=750
    ejin=11
    jiaojin=10*(-i)*(3.14159/180)/3
    changjin=pjin/(ejin-math.cos(jiaojin))
    ajin=changjin*math.cos(jiaojin)
    bjin=changjin*math.sin(jiaojin)
    jin.goto(ajin,bjin)
    
    ptu=1900
    etu=10
    jiaotu=10*(i)*(3.14159/180)/6
    changtu=ptu/(etu-math.cos(jiaotu))
    atu=changtu*math.cos(jiaotu)
    btu=changtu*math.sin(jiaotu)
    tu.goto(atu,btu)
    for zhouqi in range(3):
        jiaowei=(i/3)
        awei=(20*math.cos(jiaowei))+changtu*math.cos(jiaotu)
        bwei=(20*math.sin(jiaowei))+changtu*math.sin(jiaotu)
        wei.goto(awei,bwei)
    
    for xingxin in range(4):
        xin=tur[xingxin]
        xin.shape("circle")
        xin.speed(0)
        jiao=10*i*(3.14159/180)/(xingxin+1)
        p=po[xingxin]
        e=eo[xingxin]
        chang=p/(e-math.cos(jiao))
        a=chang*math.cos(jiao)
        b=chang*math.sin(jiao)
        xin.goto(a,b)
        
        
