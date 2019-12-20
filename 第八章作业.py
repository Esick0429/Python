class Animals:
    pass
class Mammals(Animals):
   pass
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def left_foot_forward(self):
            print('left foot forward')
    def right_foot_forward(self):
            print('right foot forward')
    def left_foot_backward(self):
            print('left foot back')
    def right_foot_backward(self):
            print('right foot back')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()
reginald = Giraffes()
reginald.dance()


# import turtle
# t1 = turtle.Pen()
# t2 = turtle.Pen()
# t3 = turtle.Pen()
# t4 = turtle.Pen()
# t1.forward(100)
# t1.left(90)
# t1.forward(50)
# t1.right(90)
# t1.forward(50)
# t2.forward(110)
# t2.left(90)
# t2.forward(25)
# t2.right(90)
# t2.forward(25)
# t3.forward(110)
# t3.right(90)
# t3.forward(25)
# t3.left(90)
# t3.forward(25)
# t4.forward(100)
# t4.right(90)
# t4.forward(50)
# t4.left(90)
# t4.forward(50)