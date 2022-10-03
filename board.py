'''
Mod
'''

from collections import namedtuple
from utils import Point, Presets, directions
from itertools import compress

from render import Renderer


class PipeType:
    PipeDir = namedtuple("FieldDir", "up right down left")
    ''' Type used to indicate possible ways leading from Field. Used only in FieldType class.
    >>> FieldDir(True, False, True, False)  # means there is path from 'up' to 'down'. '''

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
        value = PipeType.PipeDir(up, right, down, left)
        # print(value)
        values = PipeType.types.values()
        if value in values:
            sign = [(k, v) for k, v in PipeType.types.items() if v == value][0][0]
            return cls(sign)

        raise ValueError("No reprezentation with given values")


class Path(list):
    pass


class Grid:
    def __init__(self, width, height, symbol=0):
        self.width = width
        self.height = height
        self.grid = [[symbol] * width for _ in range(height)]

    def get_rows(self):
        for row in self.grid:
            yield row

    def set_symbol(self, point: Point, symbol):
        self.grid[point.y][point.x] = symbol

    @classmethod
    def as_grid(cls, grid, symbol=0):
        return cls(grid.width, grid.height, symbol)

    def draw_path(self, path: Path):
        for point in path:
            self.set_symbol(point, '*')
        return self


class Board:
    """
    Representation of game's board made out of individual Fields.
    """

    def __init__(self, presets: Presets):
        """
        :param presets: presets of board*
        """

        self.width = presets.width
        self.height = presets.height
        self.fields = [Pipe('╬')] * (self.width * self.height)
        self.start = presets.startPoint
        self.stop = presets.endPoint

        self.setup_pipes()

    def __contains__(self, point: Point):
        """
        Check whether Point is inside (right inclusive) Board.
        :param point: Point to be checked.
        :returns: bool
        """
        # FIXME ?
        # return (0 <= point.x and point.x < self.width) and (0 <= point.y and point.y < self.height)
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def get_pipe(self, point: Point) -> Pipe:
        """
        Retrieve field as Field.
        :param point: Point pointing the field.
        :returns: Character representing pipe.
        :raises IndexError: if point is not inside the Board.
        """
        if point not in self:
            raise IndexError(f"Point: {point} is not proper coordinate.")

        return self.fields[point.x + point.y * self.width]

    def get_row(self, y: int):
        """
        Retrieve fields row as characters list.
        :param y: Row index.
        :returns: Characters list representing pipe.
        :raises IndexError: if value of y is not inside the Board's height.
        """
        if Point(0, y) not in self:
            raise IndexError(f"Cannot get row with y index of {y}")

        return self.fields[0 + y * self.width: (y + 1) * self.width]

    def get_rows(self):
        """
        Generator used to retrive all rows of the Board.
        :returns: Yields rows.
        """
        for iy in range(self.height):
            yield self.get_row(iy)

    def set_pipe(self, point: Point, value: Pipe):
        """
        Set value of the field pointed by the point
        :param point: Pointed field.
        :param value: Value to be set.
        :returns: Value to be set.
        :raises IndexError: if point is not inside the Board's height.
        :raises ValueError: if value is not valid symbol.
        """
        if point not in self:
            raise IndexError(f"Point: {tuple(point)} is not proper coordinate.")

        self.fields[point.x + point.y * self.width] = value
        return value

    def get_pipe_outputs(self, point: Point):
        symbol = self.get_pipe(point).symbol
        outputs = PipeType.outputs_of(symbol)

        # Get direction of pipes outputs
        outputs = map(lambda output: output + point, outputs)

        # Filter out borders
        return filter(lambda output: output in self, outputs)

    def get_possible_ways(self, point: Point):
        outputs = self.get_pipe_outputs(point)
        outputs = filter(lambda output: point in self.get_pipe_outputs(output), outputs)
        return list(outputs)

    def _gen_checking_grid(self):
        return Grid(self.width, self.height)

    def check_connection(self, point_start: Point, point_end: Point) -> bool:
        # todo bardziej jak BFS
        checking_grid_obj = self._gen_checking_grid()
        checking_grid = checking_grid_obj.grid
        print(f"Checking connection between {point_start} and {point_end}")

        def process_using_bfs(p1, p2, depth=1):
            pass

        def process_using_dfs(p1, p2, depth=1):
            checking_grid[p1.y][p1.x] = depth

            if p1 == p2:
                print(f'Found with depth {depth}!')
                return Path([p1])

            neighbours = self.get_possible_ways(p1)

            for neighbour in neighbours:
                can_enter = checking_grid[neighbour.y][neighbour.x] == 0
                if can_enter:
                    # print(f"From {p1} entering {neighbour}")
                    tail = process_using_dfs(neighbour, p2, depth + 1)
                    if len(tail) != 0:
                        # found path to the target
                        return Path([p1]) + tail
            return Path()

        path = process_using_dfs(point_start, point_end)
        # path = process_using_bfs(point_start, point_start.up.up)
        print(path)
        print(len(path))
        # ways = self.get_possible_ways(point_start)
        # print(ways)
        # FIXME
        # for row in list(reversed(checking_grid)):
        #     print(row)
        Renderer.render(Grid.as_grid(checking_grid_obj, symbol=' ').draw_path(path))

        return True

    def setup_pipes(self):
        # self.set_field(Point(1, 0), FieldType.get_symbol_with_dirs(left=True, right=True))
        self.set_pipe(Point(1, 0), Pipe.by_dirs(up=True, down=True))
        self.set_pipe(Point(0, 1), Pipe.by_dirs(left=True, down=True, right=True))
        self.set_pipe(Point(3, 2), Pipe.by_dirs(left=True, up=True))
        self.set_pipe(Point(4, 1), Pipe.by_dirs(down=True, up=True))
        pass
