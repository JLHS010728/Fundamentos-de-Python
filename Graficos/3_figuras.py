import turtle


t = turtle.Turtle()


def dibujar_poligono(lados, longitud):
    angulo = 360 / lados
    for _ in range(lados):
        t.forward(longitud)
        t.left(angulo)

t.penup()
t.goto(-200, 0)
t.pendown()

dibujar_poligono(3, 50)

t.penup()
t.forward(50 + 50)
t.pendown()

dibujar_poligono(4, 80)

t.penup()
t.forward(80 + 100)
t.pendown()

dibujar_poligono(6, 100)