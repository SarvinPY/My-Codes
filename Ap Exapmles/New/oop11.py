import os
os.system('cls')


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(10, 20)
# print(type(point1))
point2 = Point(3, 14)
point3 = Point(6, -4)
print(point1.x, point1.y)
print(point2.x, point2.y)
