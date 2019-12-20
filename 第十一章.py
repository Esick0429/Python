import turtle
t = turtle.Pen()
t.begin_fill()
for i in range(1,9):
    t.fd(100)
    t.left(45)
t.end_fill()

# import turtle
# t = turtle.Pen()
# def star(size, points):
#     angle = 360 / points
#     for i in range(0, points):
#         t.forward(size)
#         t.left(180 - angle)
#         t.forward(size)
#         t.right(180-(angle * 2))
# star(30,5)