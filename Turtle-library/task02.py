
import turtle as t

def main():
    x1, y1 = eval(input("Enter two values for point 1: "))
    x2, y2 = eval(input("Enter two values for point 2: "))

    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    t.color("Blue")
    t.pensize(5)
    t.penup()
    t.goto(x1,y1)
    t.write("P1")
    t.pendown()
    t.goto(x2,y2)
    t.write("P2")
    t.penup()
    t.goto((x1+x2)/2,(y1+y2)/2)
    t.write(distance)
    t.hideturtle()
    t.done()

main()
