"""
AUTHOR HARIN RAMJI
FILE IS AN EXAMPLE OF CLASS CREATION AND BASICS OF OOP IN PYTHON
"""
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "the coordinate is (" + str(self.x) + "," + str(self.y) + ")"

    def __sub__(self, other):
        return Coordinate(self.x-other.x, self.y-other.y)

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5


c = Coordinate(3, 4)
o = Coordinate(0, 0)
print(c.x)
print(o.x)
print(Coordinate.distance(o, c))
print(c.distance(o))
print(c)
print(type(c))
print(isinstance(c, Coordinate))
y = Coordinate(1, 1)
print(y)
print(Coordinate.__sub__(c, y))

