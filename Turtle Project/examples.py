
# ? Design -1 Circle Spiro graph

# import turtle
# # Creating turtle
# t = turtle.Turtle()

# turtle.bgcolor("black")
# turtle.pensize(2)
# turtle.speed(0)

# for x in range(3):
#   for i in range(6):
#       for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
#           turtle.color(colors)
#           turtle.circle(100)
#           turtle.left(10)

# turtle.hideturtle()
# turtle.mainloop()


# ==================================================================================
# # ? Design - 2: Python Vibrate Circle

# import turtle
# # Creating turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pencolor("cyan")

# a = 0
# b = 0
# t.speed(0)
# t.penup()
# t.goto(0,200)
# t.pendown()
# while(True):
#     t.forward(a)
#     t.right(b)
#     a+=3
#     b+=1
#     if b == 210:
#         break
#     t.hideturtle()

# turtle.done()
# ====================================================================================
# ? Design - 3: Python Heart

import turtle
# # Creating turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")

# turtle.pensize(2)

# # To design curve
# def curve():
#     for i in range(200):
#         t.right(1)
#         t.forward(1)

# t. speed(0)
# t.color("red", "pink")

# t.begin_fill()
# t.left(140)
# t.forward(111.65)
# curve()

# t.left(120)
# curve()
# t.forward(111.65)
# t.end_fill()
# t.hideturtle()

# turtle.mainloop()
# ============================================

# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
# import turtle #Outside_In
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# skk.color("blue")

# def sqrfunc(size):
# 	for i in range(4):
# 		skk.fd(size)
# 		skk.left(90)
# 		size = size-5

# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)

# ===========================================
# import turtle #Inside_Out
# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")

# def sqrfunc(size):
# 	for i in range(4):
# 		skk.fd(size)
# 		skk.left(90)
# 		size = size + 5

# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)
# turtle.mainloop()
# ==========================================

# Python program to user input pattern
# using Turtle Programming
# import turtle #Outside_In
# import turtle
# import time
# import random

# print ("This program draws shapes based on the number you enter in a uniform pattern.")
# num_str = input("Enter the side number of the shape you want to draw: ")
# if num_str.isdigit():
# 	squares = int(num_str)

# angle = 180 - 180*(squares-2)/squares

# turtle.up

# x = 0
# y = 0
# turtle.setpos(x, y)
# turtle.bgcolor('black')

# numshapes = 8
# for x in range(numshapes):
# 	turtle.color(random.random(), random.random(), random.random())
# 	x += 5
# 	y += 5
# 	turtle.forward(x)
# 	turtle.left(y)
# 	for i in range(squares):
# 		turtle.begin_fill()
# 		turtle.down()
# 		turtle.forward(40)
# 		turtle.left(angle)
# 		turtle.forward(40)
# 		print (turtle.pos())
# 		turtle.up()
# 		turtle.end_fill()

# time.sleep(11)
# turtle.bye()

# ==========================================================

# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming

# import turtle
# loadWindow = turtle.Screen()
# turtle.speed(20)

# for i in range(80):
# 	turtle.circle(2*i)
# 	turtle.circle(-2*i)
# 	turtle.left(i)

# turtle.exitonclick()

# ===========================================================

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
# 	t.pencolor(colors[x%6])
# 	t.width(x//100 + 1)
# 	t.forward(x)
# 	t.left(59)

# ===========================================================
# import turtle
# screen=turtle.Screen()
# trtl=turtle.Turtle()
# screen.setup(620,620)
# screen.bgcolor('black')
# clr=['red','green','blue','yellow','purple']
# trtl.pensize(4)
# trtl.penup()
# trtl.pencolor('red')
# m=0
# for i in range(12):
#       m=m+1
#       trtl.penup()
#       trtl.setheading(-30*i+60)
#       trtl.forward(150)
#       trtl.pendown()
#       trtl.forward(25)
#       trtl.penup()
#       trtl.forward(20)
#       trtl.write(str(m),align="center",font=("Arial", 12, "normal"))
#       if m==12:
#         m=0
#       trtl.home()
# trtl.home()
# trtl.setpos(0,-250)
# trtl.pendown()
# trtl.pensize(10)
# trtl.pencolor('blue')
# trtl.circle(250)
# trtl.penup()
# trtl.setpos(150,-270)
# trtl.pendown()
# trtl.pencolor('olive')
# trtl.write('Vivax Solutions',font=("Arial", 12, "normal"))
# trtl.ht()
# ====================================================================
import turtle
turtle.penup()
turtle.setpos(-100,250)
turtle.pendown()
turtle.pencolor('olive')
turtle.write('Fifty Shades of Grey',font=("Arial", 18, "bold"))
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
turtle.color("black", "white")
turtle.colormode(1.0)
SQUARES = 50
SIDE = 150
shade = 1.0
for count in range(SQUARES):
  turtle.fillcolor(shade, shade, shade)
  turtle.begin_fill()
  turtle.left(360 // SQUARES)
  for side in range(4):
      turtle.forward(SIDE)
      turtle.left(90)
      turtle.end_fill()
      shade -= turtle.colormode() / float(SQUARES)
turtle.penup()
turtle.setpos(150,-270)
turtle.pendown()
turtle.done()
# ==============================================================
# import turtle

# t = turtle.Turtle()

# def square(length,angle):
#   for i in range(4):
#     t.forward(length)
#     t.right(angle)

# for i in range(200):
#   square(100,90)
#   t.right(5)

# t.done()
# ==============================================================
# import turtle 

# color = turtle.Turtle()

# color.pencolor("blue")
# for i in range(100):
#   color.forward(100)
#   color.left(123)

# color.done()