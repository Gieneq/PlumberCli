from collections import namedtuple
import types

Point = namedtuple('Point', 'x y')

class Presets:
    def __init__(self,):
        self.width = 5
        self.height = 5
        self.startPoint = Point(0, 0)
        self.endPoint = Point(self.width, self.height)
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
        # todo validate
        self.endPoint = endPoint
        return self

    def __repr__(self):
        attributes = [att for att in dir(p) if type(getattr(p, att)) != types.MethodType and '__' not in att]
        return ', '.join(map(lambda att: f"{att}={getattr(self, att)}", attributes))

p = Presets()
print(p)
