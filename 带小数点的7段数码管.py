import turtle
def drawgap():
    turtle.penup()
    turtle.fd(5)

def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawnumber(number):
    turtle.pencolor("green")
    for i in number:
        if i == '.' :
           turtle.right(90)
           turtle.fd(50)
           turtle.dot(10,"green")
           turtle.right(180)
           turtle.fd(50)
           turtle.right(90)
           turtle.fd(40)  
        else :
            drawdigit(eval(i))

def main():
    numb = input("please input a number(int or float):")
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.speed(0)
    turtle.fd(-300)
    turtle.pensize(5)
    drawnumber(numb)
    turtle.hideturtle()
    turtle.done()
main()


        