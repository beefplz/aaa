import turtle
t=turtle.Turtle()
r=50
x=0
while r <= 90:
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.circle(r)
    r=r+20
    x=x+100
    
    
