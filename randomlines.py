import turtle
import random
 
distance = 0
direction = 0
angle = 90
t1 = turtle.Turtle()
t1.pd()
t1.speed(0)
t1.color('white')
turtle.bgcolor('black')
t1.shape("square")
t1.turtlesize(stretch_len=.1, stretch_wid=.1)
t1.width(10)

while True:
    distance = random.randrange(1,101)
    direction = random.randrange(1,3)
    if direction == 1:
        t1.right(angle)
        t1.forward(distance)
    if direction == 2:
        t1.left(angle)
        t1.forward(distance)