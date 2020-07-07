import turtle

loadWindow = turtle.Screen()
turtle.speed(13)

for i in range(100):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)
    turtle.right(i)

turtle.exitonclick()