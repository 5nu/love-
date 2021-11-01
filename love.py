import turtle as t
pen1 = t.Turtle()
pen2 = t.Turtle()
pen1.color("red")
pen1.width(3)
pen2.color("red")
pen2.width(3)

pen2_name = "love"

if pen2_name == "love":
    pen2.left(40)
    pen1.left(144)

    pen2.forward(100)
    pen1.forward(100)

    for side in range(185):
        pen2.forward(1)
        pen1.forward(1)
        pen2.left(1)
        pen1.right(1)

    pen2.hideturtle()
    pen1.hideturtle()

t.done()
