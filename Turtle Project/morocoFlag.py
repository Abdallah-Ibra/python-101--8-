from turtle import * 
import turtle

def morroco_flag(taille,couleur):
  brad = turtle.Turtle(visible=False)
  brad.color(couleur)
  brad.speed(2)
  brad.width(10)
  brad.goto(-150,0)

  for _ in range(5):
    brad.forward(300)
    brad.right(180*4/5)
  
  brad.penup()
  write('Always Love Morocco ^_0', font=("Arial",15, "bold"),move=False,align='center')
  brad.end_fill()	


window = turtle.Screen()
window.bgcolor("red")
window.title("Stands With Morocco")
morroco_flag(250,"green")

window.exitonclick()
