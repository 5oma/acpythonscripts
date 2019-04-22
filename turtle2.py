import turtle
t = turtle.Pen()
z = turtle.Pen()
turtle.bgcolor("black")

for x in range(400):
    t.width(1)
    z.width(1)
    t.pencolor("red")
    z.pencolor("yellow")
    z.forward(x) 
    t.forward(x)
    t.left(25)
    z.right(35)
