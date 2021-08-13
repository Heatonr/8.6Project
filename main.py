import turtle

class Tetromino:
    blocks = []
    position = [0,0]

pen = turtle.Turtle()
screen = turtle.Screen()

pen.hideturtle()
pen.speed(0)
turtle.update()

screen.tracer(0,0)

for i in range(-6, 6):
    pen.penup()
    pen.goto(i * 30, 300)
    pen.pendown()
    pen.goto(i * 30, -300)

for i in range(-10, 12):
    pen.penup()
    pen.goto(-180, i * 30)
    pen.pendown()
    pen.goto(150, i * 30)

L_block = Tetromino()
L_block.blocks = [
    [0, 0, turtle.Turtle()],
    [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()],
    [0,0,0]
]

L_block.position[0] = -100
for y, item in enumerate(L_block.blocks):
    for x, block in enumerate(item):
        if(isinstance(block, turtle.Turtle)):
            block.penup()
            block.shape("square")
            block.turtlesize
            block.goto(x * 30 + L_block.position[0], y * 30 + L_block.position[1])
            screen.update()

turtle.mainloop()