'''
Mod
'''

from collections import namedtuple
from enum import Enum
from utils import Point, Presets



FieldDir = namedtuple("FieldDir", "up right down left")


class FieldType:
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

class Field:
    def __init__(self, symbol):
        self.symbol = symbol

    # todo rotate
    # todo check dir


class Board:
    def __init__(self, presets:Presets):
        self.width = presets.width
        self.height = presets.height
        self.fields = [' ']*(self.width*self.height)
        self.start = presets.startPoint
        self.stop = presets.endPoint

    def __contains__(self, point:Point):
        return point.x >= 0 and point.y >= 0 and point.x < self.width and point.y < self.height

    def get_field(self, point:Point):
        if point not in self:
            raise IndexError(f"Point: {point} is not proper coordinate.")
            
        return self.fields[point.x + point.y * self.width]

    def set_field(self, point:Point, value):
        if point not in self:
            raise IndexError(f"Point: {point} is not proper coordinate.")

        if FieldType.validate_sign(value):
            self.fields[point.x + point.y * self.width] = value
            return value

        raise ValueError(f"Field symbol should be: {FieldType.field_types.keys()}")

    def setup_fields():
        pass

