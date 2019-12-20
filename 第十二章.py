# from tkinter import *
# import random
# w = 400
# h = 400
# tk = Tk()
# canvas = Canvas(tk, width=w, height=h)
# canvas.pack()
# colors = ['red','green','blue','yellow','orange','white','purple']
# def random_triangle():
#     p1 = random.randrange(w)
#     p2 = random.randrange(h)
#     p3 = random.randrange(w)
#     p4 = random.randrange(h)
#     p5 = random.randrange(w)
#     p6 = random.randrange(h)
#     color = random.choice(colors)
#     canvas.create_polygon(p1, p2, p3, p4, p5, p6, \
#     fill=color, outline="")
# for x in range(0, 100):
#     random_triangle()

import time
from Tkinter import *
tk = Tk()
canvas = Canvas(tk, width=200, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 35):
    canvas.move(1, -10, 0)
    tk.update()
    time.sleep(0.05)
for x in range(0, 14):
    canvas.move(1, 0, -10)
    tk.update()
    time.sleep(0.05)