
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return (x_diff ** 2 + y_diff ** 2) ** 0.5


p1 = Point(5, 7)
print(p1)
print(p1.distance_from_origin())

p2 = Point(12, 3)
print(p2)

print(p1.distance(p2))

print(p1 == p2)

p3 = p1 + p2
print(p3)


