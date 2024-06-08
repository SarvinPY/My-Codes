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


point1 = Point(randint(0, 30), randint(0, 30))
point2 = Point(randint(0, 9), randint(0, 9))
point3 = Point(randint(10, 30), randint(10, 30))

rect1 = Rectangle(point2, point3)

point1.coordinates()
# point2.coordinates()
rect1.coordinates()


# print(point1.falls_in_rectangle(rect1))
