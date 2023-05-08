import turtle
#Settings
s = turtle.getscreen()
turtle = turtle.Turtle()
turtle.speed(200)
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.pen(pencolor="orange", pensize=3)

def draw_hexagon():
  for i in range(6):
    turtle.fd(50)
    turtle.left(60)

def draw_honeycomb():
    for i in range(6):
            draw_hexagon()
            turtle.fd(50)
            turtle.rt(60)

def five_honeycombs():
    for i in range(6):
        draw_honeycomb()
        turtle.penup()
        turtle.fd(200)
        turtle.left(60)
        turtle.pendown()
    turtle.fd(50)
    turtle.left(60)
    turtle.fd(50)
    turtle.left(60)
    turtle.fd(50)
    turtle.rt(60)
    turtle.fd(50)
    turtle.left(60)
    draw_honeycomb()

five_honeycombs()
