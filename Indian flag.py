# Program to draw Indian flag using Turtle module in python
import turtle

# Funtion to print spokes of the ashoka chakra
def spokes():
  for i in range(24):
    My_turtle.left(173)
    My_turtle.forward(49)

My_turtle = turtle.Turtle()
# My_turtle.ht()
My_turtle.shape("turtle")

def rectangle(x):
  My_turtle.speed(10)
  My_turtle.color("black",x)
  My_turtle.begin_fill()
  for i in range(2):
    My_turtle.forward(200)
    My_turtle.left(90)
    My_turtle.forward(50)
    My_turtle.left(90)
  My_turtle.end_fill()
  My_turtle.left(90)
  lifter(50)
  My_turtle.right(90)

def lifter(x):
  My_turtle.penup()
  My_turtle.forward(x)
  My_turtle.pendown()

My_turtle.penup()
My_turtle.goto(-100,-50)
My_turtle.pendown()

rectangle("green")
rectangle("white")
rectangle("orange")
My_turtle.right(90)
lifter(100)
My_turtle.left(90)
lifter(100)

My_turtle.color('blue')
My_turtle.circle(25)
My_turtle.left(90)
My_turtle.forward(50)

spokes()
My_turtle.penup()
My_turtle.showturtle()
My_turtle.goto(-80,-100)

My_turtle.color("#ff4500")
My_turtle.write("JAI HIND", font=("Arial", 30, "normal"))
My_turtle.ht()

input()
