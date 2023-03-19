# Import required module
import turtle

# Create turtle object
t = turtle.Turtle()

# Create a screen 
screen =turtle.Screen()

# Set background color
screen.bgcolor("yellow")

# Function to draw body of snowman
def draw_circle(color, radius, x, y):
    t.pensize(2)
    t.penup()
    t.fillcolor (color)
    t.goto (x, y)
    t.pendown()
    t.begin_fill()
    t.circle (radius)
    t.end_fill()

# Function to draw arms 
def create_line(x, y, length, angle):
    t.pensize(2)
    t.color('red')
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.setheading(angle + 20)
    t.forward(20)
    t.penup()
    t.back(20)
    t.pendown()
    t.setheading(angle - 20)
    t.forward(20)
    t.penup()
    t.home()


# Illustrating snowman 
# Drawing snowman body
draw_circle ("#ffffff", 30, 0, -40)
draw_circle ("#ffffff", 40, 0, -100)
draw_circle ("#ffffff", 60, 0, -200)

# Drawing left eye
draw_circle ("#ffffff", 2, -10, -10) 
# Drawing right eye
draw_circle ("#ffffff", 2, 10, -10) 
# Drawing nose
draw_circle ("#FF6600", 3, 0, -15)  
# Drawing buttons on
draw_circle ("#ffffff", 2, 0, -35)
draw_circle ("#ffffff", 2, 0, -45)
draw_circle ("#ffffff", 2, 0, -55)


create_line(10, -270, 50, 90) 
create_line(-10, -270, 50, 90) 
# Drawing left arm
create_line(-50, -50, 50, 140) 
# Drawing right arm
create_line(50, -50, 50, 40) 
