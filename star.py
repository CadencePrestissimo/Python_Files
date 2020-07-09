import turtle
from turtle import *
color('black', 'grey')
turtle.speed(20)
turtle.width(2)
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()