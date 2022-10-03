from collections import namedtuple

# def gen_x_coord_labels(x_count: int):
#     return [str(x + 1) for x in range(x_count)]
#
#
# def gen_y_coord_labels(y_count: int):
#     return [str(chr(ord('A') + y)) for y in range(y_count)]


_Point = namedtuple('Point', 'x y')


class Point(_Point):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def is_inside(self, width: int, height: int) -> bool:
        return 0 <= self.x < width and 0 <= self.y < height

    @property
    def up(self):
        return self + Point(0, 1)

    @property
    def down(self):
        return self + Point(0, -1)

    @property
    def right(self):
        return self + Point(1, 0)

    @property
    def left(self):
        return self + Point(-1, 0)


directions = Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)
