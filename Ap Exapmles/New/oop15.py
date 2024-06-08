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


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


point1 = Point(10, 20)
# print(type(point1))
point2 = Point(30, 140)
point3 = Point(-6, -4)
print(point1.x, point1.y)

rect1 = Rectangle(point3, point2)

print(point1.falls_in_rectangle(rect1))
