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
        canvas.forward(rect1.upright.x-rect1.lowleft.x)
        canvas.left(90)
        canvas.forward(rect1.upright.y-rect1.lowleft.y)
        canvas.left(90)
        canvas.forward(rect1.upright.x-rect1.lowleft.x)
        canvas.left(90)
        canvas.forward(rect1.upright.y-rect1.lowleft.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


point1 = GuiPoint(randint(-100, 250), randint(-100, 250))
point2 = Point(randint(-100, +100), randint(-100, +100))
point3 = Point(randint(101, 250), randint(101, 250))

rect1 = GuiRectangle(point2, point3)

point1.coordinates()
rect1.coordinates()

print(rect1.area())

print(point1.falls_in_rectangle(rect1))
myturtle = turtle.Turtle()
rect1.draw(myturtle)
point1.draw(myturtle, 8, 'blue')
turtle.done()
# myturtle.penup()
# myturtle.goto(100, 50)
