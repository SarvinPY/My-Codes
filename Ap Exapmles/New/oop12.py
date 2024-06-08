import os
os.system('cls')


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft.x < self.x < upright.x \
                and lowleft.y < self.y < upright.y:
            return True
        else:
            return False


point1 = Point(10, 13)
# print(type(point1))
point2 = Point(0, 11)
point3 = Point(10, 25)
# print(point1.x, point1.y)

print(point1.falls_in_rectangle(point2, point3))
