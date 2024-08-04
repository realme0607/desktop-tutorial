#1.Develop a program to draw a line using Bresenham’s line drawing technique.
import turtle

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x_step = 1 if x1 < x2 else -1
    y_step = 1 if y1 < y2 else -1
    error = dx - dy
    line_points = []
    x, y = x1, y1
    while True:
        line_points.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x += x_step
        if e2 < dx:
            error += dx
            y += y_step
    return line_points

# Set up the turtle window
turtle.setup(500, 500)
turtle.speed(0)  # Fastest drawing speed

# Define start and end points
x1, y1 = 100, 100
x2, y2 = 400, 300

# Get the line points using Bresenham's algorithm
line_points = bresenham_line(x1, y1, x2, y2)

# Draw the line using Turtle
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
for x, y in line_points:
    turtle.goto(x, y)

turtle.exitonclick()
 