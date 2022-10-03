from collections import namedtuple
import types


def gen_x_coord_labels(x_count: int):
    return [str(x + 1) for x in range(x_count)]


def gen_y_coord_labels(y_count: int):
    return [str(chr(ord('A') + y)) for y in range(y_count)]


_Point = namedtuple('Point', 'x y')


class Point(_Point):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

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


class Presets:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.startPoint = Point(0, 0)
        self.endPoint = Point(self.width - 1, self.height - 1)
        # todo algorithm type

    def with_width(self, width):
        self.width = width
        return self

    def with_height(self, height):
        self.height = height
        return self

    def with_start_point(self, startPoint):
        self.startPoint = startPoint
        return self

    def with_end_point(self, endPoint):
        self.endPoint = endPoint
        return self

    def validate(self):
        if not self.startPoint.is_inside(self.width, self.height):
            raise IndexError(f"Point: {self.startPoint} is not proper coordinate.")

        if not self.endPoint.is_inside(self.width, self.height):
            raise IndexError(f"Point: {self.endPoint} is not proper coordinate.")

        return self

    @staticmethod
    def build_from_args(args):
        return Presets().with_width(args.width).with_height(args.height).with_start_point(
            Point(*args.start)).with_end_point(
            Point(*args.end)).validate()

    def __repr__(self):
        attributes = [att for att in dir(self) if type(getattr(self, att)) != types.MethodType and '__' not in att]
        return ', '.join(map(lambda att: f"{att}={getattr(self, att)}", attributes))
