from collections import namedtuple
import types

Point = namedtuple('Point', 'x y')

def is_point_inside(p:Point, width:int, height:int) -> bool:
    return p.x >=0 and p.y >= 0 and p.x < width and p.y < height

class Presets:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.startPoint = Point(0, 0)
        self.endPoint = Point(self.width-1, self.height-1)
        # todo algorithm type

    def withWidth(self, width):
        self.width = width
        return self

    def withHeight(self, height):
        self.height = height
        return self

    def withStartPoint(self, startPoint):
        self.startPoint = startPoint
        return self

    def withEndPoint(self, endPoint):
        self.endPoint = endPoint
        return self

    def validate(self):
        if not is_point_inside(self.startPoint, self.width, self.height):
            raise IndexError(f"Point: {self.startPoint} is not proper coordinate.")

        if not is_point_inside(self.endPoint, self.width, self.height):
            raise IndexError(f"Point: {self.endPoint} is not proper coordinate.")

        return self


    @staticmethod
    def buildFromArgs(args):
        return Presets().withWidth(args.width).withHeight(args.height).withStartPoint(Point(*args.start)).withEndPoint(Point(*args.end)).validate()

    def __repr__(self):
        attributes = [att for att in dir(self) if type(getattr(self, att)) != types.MethodType and '__' not in att]
        return ', '.join(map(lambda att: f"{att}={getattr(self, att)}", attributes))
