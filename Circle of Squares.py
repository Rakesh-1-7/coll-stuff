import turtle
T = turtle.Turtle()
T.speed(50)
def square(length,angle):
    T.pencolor("dark green")
    for i in range(4):
        T.forward(length)
        T.right(angle)
    T.pencolor("orange")
    T.right(11)
    for i in range(4):
        T.forward(length)
        T.right(angle)
    
        
    T.right(11)
for i in range(150):
    square( 100 , 90)
