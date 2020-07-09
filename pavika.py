from turtle import Turtle, Screen
from math import sqrt
NAME = "PAVIK1"

BORDER = 1
BOX_WIDTH, BOX_HEIGHT = 6, 10
WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2
def letter_P(turtle):
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.circle(-WIDTH/2,180,30)

def letter_A(turtle):
    turtle.penup()
    turtle.goto(WIDTH , 1)
    turtle.pendown()
    turtle.left(0.20 * -90)
    turtle.forward(sqrt(70))
    turtle.left(-145)
    turtle.forward(sqrt(70))
    turtle.penup()
    turtle.goto(WIDTH*1.26,HEIGHT/2)
    turtle.right(0.20 * -90-55)
    turtle.pendown()
    turtle.forward(3.10)

def letter_V(turtle):
    turtle.penup()
    turtle.goto(WIDTH*3,1)
    turtle.pendown()
    turtle.left(20.5)
    turtle.forward(sqrt(74))
    turtle.penup()
    turtle.goto(WIDTH * 3, 1)
    turtle.pendown()
    turtle.right(20.5*2)
    turtle.forward(sqrt(74))


def letter_I(turtle):
    turtle.penup()
    turtle.goto(WIDTH*4, 1)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(WIDTH)
    turtle.backward(WIDTH / 2)
    turtle.left(90)
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.backward(WIDTH / 2)
    turtle.forward(WIDTH)

def letter_K(turtle):
    turtle.penup()
    turtle.goto(WIDTH*5.5, 1)
    turtle.pendown()
    turtle.forward(HEIGHT)
    turtle.penup()
    turtle.goto(WIDTH * 5.5, HEIGHT/2+1)
    turtle.pendown()
    turtle.right(45.5)
    turtle.forward(sqrt(32))
    turtle.penup()
    turtle.goto(WIDTH * 5.5, HEIGHT / 2+1)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(sqrt(32))


def letter_A1(turtle):
    turtle.penup()
    turtle.goto(7*WIDTH , 1)
    turtle.pendown()
    turtle.left(0.20 * -90)
    turtle.forward(sqrt(70))
    turtle.left(-145)
    turtle.forward(sqrt(70))
    turtle.penup()
    turtle.goto(WIDTH*(1.26+6),HEIGHT/2)
    turtle.right(0.20 * -90-55)
    turtle.pendown()
    turtle.forward(3.10)

LETTERS = { 'P': letter_P,'A': letter_A,'V':letter_V,'I': letter_I,'K':letter_K,'1': letter_A1}

wn = Screen()
wn.setup(800, 400)
wn.title("Turtle writing my name: {}".format(NAME))
wn.setworldcoordinates(0, 0, BOX_WIDTH * len(NAME), BOX_HEIGHT)

marker = Turtle()
marker.width(4)
for counter, letter in enumerate(NAME):
    marker.penup()
    marker.goto(counter * BOX_WIDTH + BORDER, BORDER)
    marker.setheading(90)

    if letter in LETTERS:
        marker.pendown()
        LETTERS[letter](marker)

marker.hideturtle()

wn.mainloop()