import fractions
from fractions import Fraction

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, point_text):
        self.x, self.y = list(map(int, point_text.split()))

    def is_above(self, line):
        return self.y > line.get_y_at(self.x)

    def is_on(self, line):
        return self.y == line.get_y_at(self.x)

    def is_below(self, line):
        return self.y < line.get_y_at(self.x)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)


class Line:
    def __init__(self, fraction_text, constant = 0):
        numerator, denominator = list(map(int, fraction_text.split('/')))

        self.a = Fraction(numerator, denominator)
        self.b = Fraction(constant, 1)
    
    def shift_to_contain(self, point):
        self.b = point.y - self.a * point.x

    def get_y_at(self, x):
        return self.a * x + self.b
    
    def __repr__(self):
        return '({})*x + {}'.format(self.a, self.b)


if __name__ == '__main__':
    n = int(input())

    a1_line, a2_line = list(map(Line, input().split()))

    points = []
    valid_points = set()
    for i in range(n):
        points.append(Point(input()))
        if points[-1].is_above(a1_line) and points[-1].is_below(a2_line):
            valid_points.add(points[-1])

    for point in valid_points:
        print(point)

    