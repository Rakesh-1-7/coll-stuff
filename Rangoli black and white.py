import turtle
T = turtle.Turtle()
T.speed(0)
def cut_square():

	for i in range(4):
		
		T.penup()
		T.forward(100)
		T.pendown()
		T.forward(50) 
		T.right(270)

for i in range (50):
	cut_square()
	T.right(51)
