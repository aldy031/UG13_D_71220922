def manggil():
    import turtle
    pen1 = turtle.Turtle()
    pen1.screen.bgcolor("blue")
    pen1.pensize(25)
    pen1.pencolor("white")
    
    pen1.circle(80,180)
    pen1.left(90)
    pen1.forward(290)
    pen1.backward(110)
    pen1.left(45)
    pen1.forward(150)
    pen1.up()
    pen1.goto(50,200)
    pen1.right(150)
    
    pen1 = turtle.Screen().exitonclick()

manggil()