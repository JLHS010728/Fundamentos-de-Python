import turtle

t = turtle.Turtle()
t.left(10)
for _ in range(4):
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.left(15)  