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

    def distance_from_point(self, point):
        return ((self.x-point.x)**2 + (self.y-point.y)**2)**0.5
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


point1 = Point(10, 20)
# print(type(point1))
point2 = Point(30, 140)
point3 = Point(-600, -400)
point4 = Point(12, 13)
# print(point1.x, point1.y)

# print(point1.falls_in_rectangle(point3, point2))
print(point1.distance_from_point(point3))
print(point2.distance_from_point(point4))
print(point1)
