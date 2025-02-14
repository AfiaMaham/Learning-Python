import turtle as t

def main():

    t.color("red")
    t.pensize(5)
    t.penup()

    #  triangle
    t.goto(-200,-50)
    t.pendown()
    t.circle(40,steps = 3)

    t.penup()
    t.goto(-100,-50)
    t.pendown()
    t.circle(40, steps = 4)

    t.penup()
    t.goto(0,-50)
    t.begin_fill()
    t.pendown()
    t.circle(40, steps = 5)
    t.end_fill()

    t.penup()
    t.goto(100,-50)
    t.pendown()
    t.circle(40, steps = 6) 

    t.penup()
    t.goto(200,-50)
    t.pendown()
    t.circle(40, steps = 7)

    t.hideturtle()
    t.done()


main()