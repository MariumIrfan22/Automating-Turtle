#!/usr/bin/env python
# coding: utf-8

# # Automating Turtle Graphics

# In[1]:


#double smiley face
#jump function
def jump(t,x,y):
    'easy to jump to another point instead of penup and pendown'
    t.penup()
    t.goto(x,y)
    t.pendown()
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def smileyface(t,x,y):
    'this create a smiley face'
    t.pensize(3)
    t.setheading(0)
    jump(t,x,y)
    t.circle(100)
    jump(t,x+35,y+120)
    t.dot(25)
    jump(t,x-35,y+120)
    t.dot(25)
    jump(t,x-60.62,y+65)
    t.setheading(-60)
    t.circle(70,120)
smileyface(t,-100,100)
smileyface(t,150,100)


# In[2]:


#CS.13(double smiley)
#jump function
def jump(t,x,y):
    'easy to jump to another point instead of penup nad pendown'
    t.penup()
    t.goto(x,y)
    t.pendown()
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def olympic(t):
    t.pensize(3)
    jump(t,0,0)
    t.setheading(0)
    t.circle(100)
    jump(t,-220,0)
    t.circle(100)
    jump(t,220,0)
    t.circle(100)
    jump(t,-110,-100)
    t.circle(100)
    jump(t,110,-100)
    t.circle(100)
olympic(t)


# In[1]:


#CS.14(polygon)
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def polygon(t):
    n=int(input("enten the number of sides of polygon:"))
    for i in range(1,n):
        t.forward(100)
        t.left(35)
    t.goto(0,0)
polygon(t)


# In[1]:


#CS.15(grid)
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def grid(m,n):
    x=0
    y=0
    for i in range(m):
        for j in range(n):
            t.penup()
            t.goto(x,y)
            t.pendown()
            box()
            x+=75
        y-=75
        x=0
        t.penup()
        t.goto(x,y)
        t.pendown()

            
def box():
    for i in range(4):
        t.forward(75)
        t.right(90)
grid(2,2)


# In[2]:


#CS.16 (spiral)
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def square(l,ang):
     for i in range(1,5):
        t.forward(l)
        t.right(90)
def spiral(l,ang,mul):
    for i in range(1,5):
        t.forward(l)
        t.right(90)
    t.speed(400)
    t.pensize(3)
    for i in range(1,mul+1):
        square(l,ang)
        t.right(10)
spiral(50,90,37)
    


# In[ ]:


#CS.17(planets)
def jump(t,x,y):
    'easy to jump to another point instead of penup nad pendown'
    t.penup()
    t.goto(x,y)
    t.pendown()
import turtle
s=turtle.Screen()
z=turtle.Turtle()
z.shape('circle')
a=turtle.Turtle()
a.shape('circle')
b=turtle.Turtle()
b.shape('circle')
c=turtle.Turtle()
c.shape('circle')
d=turtle.Turtle()
d.shape('circle')
jump(z,0,0)
jump(a,0,-58)
jump(b,0,-108)
jump(c,0,-150)
jump(d,0,-228)
i=True
while i==True:
    a.speed(100)
    b.speed(100)
    c.speed(100)
    d.speed(100)
    for j in range(7):
        a.circle(58,1)
    for j in range(3):
        b.circle(108,1)
    for j in range(2):
        c.circle(150,1)
    for j in range(1):
        d.circle(228,1)
              


# In[ ]:




