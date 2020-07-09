import turtle

t = turtle.Turtle()
t.speed(20);
r = 10
for i in range(700):
    t.circle(r + i*0.5, 60)
