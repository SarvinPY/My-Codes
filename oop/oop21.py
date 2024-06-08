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


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()
        canvas.forward(self.upright.x-self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y-self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x-self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y-self.lowleft.y)


# point1 = Point(randint(0, 30), randint(0, 30))
point2 = Point(randint(-100, +100), randint(-100, +100))
point3 = Point(randint(101, 250), randint(101, 250))

rect1 = GuiRectangle(point2, point3)

rect1.coordinates()

print(rect1.area())


myturtle = turtle.Turtle()
rect1.draw(myturtle)
# turtle.done()
# myturtle.penup()
# myturtle.goto(100, 50)
