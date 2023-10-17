import turtle

turtle.penup()
x, y = 0, 0
turtle.goto(x, y)

with open('picture.txt') as f:
    for line in f:
        if not line.strip():
            turtle.penup()
        else:
            x, y = map(int, line.split(','))
            turtle.pendown()
            turtle.goto(x, y)

turtle.done()