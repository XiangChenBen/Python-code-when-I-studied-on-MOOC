import turtle
import math
def dragon(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in (45,-90,-90,90):
            turtle.left(angle)
            dragon(size/math.sqrt(2),n-1)
        turtle.right(135)


           
def main():
    turtle.setup(800,600)
    turtle.penup()
    turtle.goto(-300,-100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(5)
    level = 1
    dragon(200,level)
    turtle.hideturtle()
    turtle.done()
main()