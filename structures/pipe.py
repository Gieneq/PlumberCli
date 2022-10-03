from collections import namedtuple
from itertools import compress
from utils.point import directions

PipeDir = namedtuple("FieldDir", "up right down left")
""" Type used to indicate possible ways leading from Field. Used only in FieldType class.
>>> FieldDir(True, False, True, False)  # means there is path from 'up' to 'down'.  """


class PipeType:
    types = {
        '╬': PipeDir(True, True, True, True),
        ' ': PipeDir(False, False, False, False),

        '║': PipeDir(True, False, True, False),
        '═': PipeDir(False, True, False, True),

        '╩': PipeDir(True, True, False, True),
        '╠': PipeDir(True, True, True, False),
        '╦': PipeDir(False, True, True, True),
        '╣': PipeDir(True, False, True, True),

        '╚': PipeDir(True, True, False, False),
        '╔': PipeDir(False, True, True, False),
        '╗': PipeDir(False, False, True, True),
        '╝': PipeDir(True, False, False, True),
    }

    @classmethod
    def outputs_of(cls, sign):
        field_dir = cls.types[sign]
        return list(compress(directions, field_dir))

    @classmethod
    def validate_symbol(cls, symbol):
        return symbol in cls.types.keys()


class Pipe:
    def __init__(self, sign):
        # sign cannot be changed
        self._sign = sign

    def rotate(self, n_turns: int):
        pass

    @property
    def symbol(self):
        return self._sign

    def __str__(self):
        return self._sign

    @classmethod
    def by_dirs(cls, up=False, right=False, down=False, left=False):
        value = PipeDir(up, right, down, left)
        # print(value)
        values = PipeType.types.values()
        if value in values:
            sign = [(k, v) for k, v in PipeType.types.items() if v == value][0][0]
            return cls(sign)

        raise ValueError("No reprezentation with given values")
