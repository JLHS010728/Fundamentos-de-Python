import turtle
t = turtle.Turtle()

def linea_punteada(longitud):
    for _ in range(longitud // 10):
        t.pendown()
        t.forward(5)
        t.penup()
        t.forward(5)


t.penup()
t.goto(-50, 0)  
t.setheading(0)  
linea_punteada(100)


t.penup()
t.goto(-75, -50)  
t.setheading(0)
linea_punteada(150)
