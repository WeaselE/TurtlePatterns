import turtle
import random
import numpy as np

color_choices = ["cyan", "white", "light green", "green", "purple", "pink", "red", "orange"]
#Turtle necessary setup
def Setup():
    t = turtle.Turtle()
    t.setpos((300, 300))
    t.pendown()
    t.color('cyan')
    turtle.bgcolor('black')
    # turtle.screensize(1280, 720)
    window = turtle.Screen()
    window.screensize(1920, 1080)
    window.setup(width=1.0, height=1.0)
    t.speed(0)
    return t

#Shape functions
def Square():
    t = Setup()
    #forever loop
    while True:
        #Square Setup
        t.penup()
        size = random.randrange(20, 201)
        posx = random.randrange(-900, 900)
        posy = random.randrange(-640, 640)
        t.color(random.choice(color_choices))
        t.setpos((posx, posy))
        #Draw Square
        t.pendown()
        for i in range(4):
            t.forward(size)
            t.right(90)

def Circle():
    t = Setup()
    while True:
        #Circle Setup
        t.penup()
        size = random.randrange(20, 201)
        posx = random.randrange(-900, 900)
        posy = random.randrange(-640, 640)
        t.color(random.choice(color_choices))
        t.setpos((posx, posy))
        #Draw circle
        t.pendown()
        t.circle(size)
    

def Triangle():
    t = Setup()
    while True:
        #Triangle Setup
        t.penup()
        size = random.randrange(20, 201)
        posx = random.randrange(-900, 900)
        posy = random.randrange(-640, 640)
        angle = 120
        t.color(random.choice(color_choices))
        t.setpos((posx, posy))
        #Draw Triangle
        t.pendown()
        for i in range(3):
            t.forward(size)
            t.left(angle)
    pass

def Rectangle():
    t = Setup()
    while True:
        #Rectangle Setup
        t.penup()
        size1 = random.randrange(20, 201)
        size2 = random.randrange(20, 201)
        posx = random.randrange(-900, 900)
        posy = random.randrange(-640, 640)
        t.color(random.choice(color_choices))
        t.setpos((posx, posy))
        #Rectangle Draw
        t.pendown()
        for i in range(2):
            t.forward(size1)
            t.right(90)
            t.forward(size2)
            t.right(90)
    pass

def Random():
    x = random.randrange(0, 4)
    print(x)
    if x == 0:
        Square()
    elif x == 1:
        Circle()
    elif x == 2:
        Triangle()
    elif x == 3:
        Rectangle()

def print_choices():
    print("Options are 1, 2, 3, 4, 5.")
    print()
    print("(1) Draw squares")
    print()
    print("(2) Draw circles")
    print()
    print("(3) Draw triangles")
    print()
    print("(4) Draw rectangles")
    print()
    print("(5) Draw random shape")

if __name__=="__main__":
    print_choices()
    try:
        choice = int(input("Please input your choice as the number given: "))
    except Exception:
        choice = -1
    #If choice is sqaures
    if choice == 1:
        Square()
    #If choice is circles
    if choice == 2:
        Circle()
    #If choice is triangles
    if choice == 3:
        Triangle()
    #If choice is rectangles
    if choice == 4:
        Rectangle()
    #If choice is random
    if choice == 5:
        Random()
    #If choice is invalid
    if choice == -1:
        print("input given was not valid input.")