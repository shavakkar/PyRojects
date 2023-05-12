import turtle

turtle.bgcolor("white")
turtle.pensize(5)
turtle.speed(0.2)
colours = ["green","red","yellow","cyan"]
for i in range(20):
    for color in colours:
        turtle.color(color)
        turtle.circle(120)
        turtle.left(15)


turtle.mainloop()