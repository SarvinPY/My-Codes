import turtle

from random import randint
import os
os.system('cls')


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x-point.x)**2 + (self.y-point.y)**2)**0.5

    def coordinates(self):
        print("-------Point Coordinates------")
        print("X : {}      Y: {}".format(self.x, self.y))
        print("-----------------------------")


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def coordinates(self):
        print("------Recangle Coordinates-----")
        print("Up Right:({} , {})".format(self.upright.x, self.upright.y))
        print("Low Left:({} , {})".format(self.lowleft.x, self.lowleft.y))
        print("-----------------------------")

    def area(self):
        return (self.upright.x-self.lowleft.x) * \
            (self.upright.y-self.lowleft.y)


# point1 = Point(randint(0, 30), randint(0, 30))
point2 = Point(randint(-100, +100), randint(-100, +100))
point3 = Point(randint(101, 250), randint(101, 250))

rect1 = Rectangle(point2, point3)

rect1.coordinates()

print(rect1.area())


myturtle = turtle.Turtle()
myturtle.penup()
myturtle.goto(rect1.lowleft.x, rect1.lowleft.y)
myturtle.pendown()
myturtle.forward(rect1.upright.x-rect1.lowleft.x)
myturtle.left(90)
myturtle.forward(rect1.upright.y-rect1.lowleft.y)
myturtle.left(90)
myturtle.forward(rect1.upright.x-rect1.lowleft.x)
myturtle.left(90)
myturtle.forward(rect1.upright.y-rect1.lowleft.y)

# myturtle.penup()
# myturtle.goto(100, 50)
turtle.done()
