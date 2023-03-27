import turtle
for i in range(19):
    turtle.circle(100, 360, 4)  # draw a square
    turtle.penup()
    # "draw" 10 degrees of the same circle, with the pen up, just to move the pen
    turtle.circle(100, 10, 4)
    turtle.pendown()