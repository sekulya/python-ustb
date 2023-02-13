#importing required modules
#导入所需的模块
from turtle import * 
from random import *
#assign all the trees to turtle
#将所有树木分配给乌龟
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()
t7 = Turtle()
t8 = Turtle()
t9 = Turtle()
t10 = Turtle()
#loop to draw goto point of trees and its speed,color
#绘制树木的转到点及其速度，颜色的功能
x = -200
turtles = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
for t in turtles:
  t.speed(100)
  t.left(70)
  t.color('brown')
  t.pu()
  x += randint(60,140)
  t.goto(x, randint(-50,50))
  t.pd()

#branch's angle,size,sf,color and length
#分支的角度，大小，sf，颜色和长度
def branch(turt, branch_len):
  angle = randint(20,25)
  sf = uniform(0.6,0.8)
  size = int(branch_len /10)
  turt.pensize(size)
  #如果分支长度小于20
  if branch_len < 20:
    turt.color('pink')
    turt.stamp()
    turt.color('brown')
  #如果分支长度大于10
  if branch_len > 10:
    turt.forward(branch_len)
    turt.left(angle)
    branch(turt, branch_len*sf)
    turt.right(angle*2)
    branch(turt, branch_len*sf)
    turt.left(angle)
    turt.backward(branch_len)
#loop
#环形
for t in turtles:
  branch(t,100)
turtles.mainloop()
