import turtle
turtle.color('black')
turtle.speed(5)

c = 0
while c < 4:
    c += 1
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)

turtle.exitonclick()