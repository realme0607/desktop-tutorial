#2. Develop a program to demonstrate basic geometric operations on the 2D object
import turtle
import math

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(1) 
t.pensize(2)

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)

def translate(x, y, dx, dy):
    return x + dx, y + dy

def rotate(x, y, angle):
    radians = math.radians(angle)
    new_x = x * math.cos(radians) - y * math.sin(radians)
    new_y = x * math.sin(radians) + y * math.cos(radians)
    return new_x, new_y

def scale(x, y, sx, sy):
    return x * sx, y * sy

# Draw the rectangles
x, y = -200, 0
draw_rectangle(x, y, 100, 50, "blue")

x, y = translate(x, y, 200, 0)
draw_rectangle(x, y, 100, 50, "blue")

x, y = rotate(x, y, 45)
draw_rectangle(x, y, 100, 50, "blue")

x, y = scale(x, y, 2, 2)
draw_rectangle(x, y, 100, 50, "blue")

# Draw the circles
x, y = 100, 100
draw_circle(x, y, 50, "red")

x, y = translate(x, y, 200, 0)
draw_circle(x, y, 50, "red")

x, y = rotate(x, y, 45)
draw_circle(x, y, 50, "red")

x, y = scale(x, y, 2, 2)
draw_circle(x, y, 50, "red")

# Finish drawing
turtle.done()
