import turtle
t = turtle.Turtle()
t.width(12)
t.color("blue")
t.circle(50)
number = 60
while number <= 240:
    t.penup()
    t.goto(number,-50)
    t.pendown()
    if number==60:
        t.color("yellow")
    elif number==180:
        t.color("green")
    t.circle(50)
    number = number + 60
    t.penup()
    t.goto(number,0)
    t.pendown()
    if number==120:
        t.color("black")
    elif number==240:
        t.color("red")
    t.circle(50)
    number = number + 60
