import turtle as t

def main():
    x1, y1 = eval(input("Enter two values for point 1: "))
    x2, y2 = eval(input("Enter two values for point 2: "))
    x3 = eval(input("Enter radius: "))
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5

    t.color("red")
    t.pensize(3)
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(x3)
    t.penup()
    t.goto(x2,y2)
    t.begin_fill()
    t.color("purple")
    t.pendown()
    t.circle(2)
    t.goto(x2,y2+3)
    t.write("P1")
    t.end_fill()
    t.penup()
    t.goto(x1-x3, y1-x3)
    if distance <= x3:
        t.write("point p1 is inside", font=("Times",10))
    else:
        t.write("point p1 is outside")
    t.hideturtle()
    t.done()

main()
