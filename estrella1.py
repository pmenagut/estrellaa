import turtle

def draw_star(steps, length, colors):
    angle = 180 - (180 / steps)

    for c in colors:
        turtle.pencolor(c)

        for i in range(steps):
            turtle.forward(length)
            turtle.right(angle)
            turtle.forward(length)
            turtle.left(360 / steps)

    turtle.done()

colors = ['blue', 'red', 'green']
draw_star(5, 200, colors)