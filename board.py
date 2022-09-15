'''
Mod
'''

from collections import namedtuple
from enum import Enum


Point = namedtuple('Point', 'x y')


FieldDir = namedtuple("FieldDir", "up right down left")


class Fields:
    field_types = {
        '╬': FieldDir(True, True, True, True),
        ' ': FieldDir(False, False, False, False),

        '║': FieldDir(True, False, True, False),
        '═': FieldDir(False, True, False, True),

        '╩': FieldDir(True, True, False, True),
        '╠': FieldDir(True, True, True, False),
        '╦': FieldDir(False, True, True, True),
        '╣': FieldDir(True, False, True, True),

        '╚': FieldDir(True, True, False, False),
        '╔': FieldDir(False, True, True, False),
        '╗': FieldDir(False, False, True, True),
        '╝': FieldDir(True, False, False, True),
    }

    @classmethod
    def validate_sign(cls, sign):
        return sign in cls.field_types.keys()


class Board:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.fields = [' ']*(width*height)
        self.start = Point(0,0)
        self.stop = Point(width - 1, height - 1)

    def __contains__(self, point:Point):
        return point.x >= 0 and point.y >= 0 and point.x < self.width and point.y < self.height

    def get_field(self, point:Point):
        if point not in self:
            raise IndexError(f"Point: {point} is not proper coordinate.")
            
        return self.fields[point.x + point.y * self.width]

    def set_field(self, point:Point, value):
        if point not in self:
            raise IndexError(f"Point: {point} is not proper coordinate.")

        if Fields.validate_sign(value):
            self.fields[point.x + point.y * self.width] = value
            return value

        raise ValueError(f"Field symbol should be: {Fields.field_types.keys()}")

    def setup_fields():
        pass

