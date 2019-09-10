import turtle
turtle.speed(5000)


def star(turtle,size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


size = 1
for i in range(50):
    star(turtle,size)
    size = size + 4
    turtle.forward(1)
    turtle.right(8)

turtle.penup()
turtle.goto(-350, 200)
turtle.pendown()
turtle.color("red")


def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)


for i in range(60):
    square(200)
    turtle.right(5)
turtle.penup()
turtle.goto(425, 200)
turtle.pendown()

def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)


for i in range(60):
    square(200)
    turtle.right(5)


turtle.penup()
turtle.goto(135, -350)
turtle.pendown()

turtle.circle(100)





turtle.exitonclick()