import turtle
t = turtle.Turtle()
t.circle(50)
number = 120
while number <= 240:
    t.penup()
    t.goto(number,0)
    t.pendown()
    t.circle(50)
    number = number + 120
number = 60
while number <= 180:
    t.penup()
    t.goto(number,-50)
    t.pendown()
    t.circle(50)
    number = number + 120
