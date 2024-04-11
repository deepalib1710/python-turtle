import turtle
wn = turtle.Screen()
wn.title("DNT Writing with Turtle")
writer = turtle.Turtle()
writer.speed("slow")

def draw_D():
    writer.penup()
    writer.goto(-100, 0)
    writer.pendown()
    writer.left(90)
    writer.forward(100)
    writer.right(90)
    writer.circle(-50, 180)

def draw_N():
    writer.penup()
    writer.goto(-30, -100)
    writer.pendown()
    writer.left(90)
    writer.forward(100)
    writer.right(135)
    writer.forward(140)
    writer.left(135)
    writer.forward(100)

def draw_T():
    writer.penup()
    writer.goto(70, 0)
    writer.pendown()
    writer.left(90)
    writer.forward(100)
    writer.right(90)
    writer.forward(25)
    writer.backward(50)

draw_D()
draw_N()
draw_T()

writer.hideturtle()
wn.mainloop()
