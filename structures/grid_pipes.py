from utils.point import Point
from utils.search import check_connection
from structures.grid import Grid
from structures.pipe import Pipe, PipeType
import types


class Presets:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.start_point = Point(0, 0)
        self.end_point = Point(self.width - 1, self.height - 1)
        self.base_symbol = 0
        # todo algorithm type

    def with_width(self, width):
        self.width = width
        return self

    def with_height(self, height):
        self.height = height
        return self

    def with_start_point(self, start_point):
        self.start_point = start_point
        return self

    def with_end_point(self, end_point):
        self.end_point = end_point
        return self

    def with_base_symbol(self, base_symbol):
        self.base_symbol = base_symbol
        return self

    def validate(self):
        if not self.start_point.is_inside(self.width, self.height):
            raise IndexError(f"Point: {self.start_point} is not proper coordinate.")

        if not self.end_point.is_inside(self.width, self.height):
            raise IndexError(f"Point: {self.end_point} is not proper coordinate.")

        return self

    @staticmethod
    def build_from_args(args):
        return Presets().with_width(args.width).with_height(args.height).with_start_point(
            Point(*args.point_start)).with_end_point(
            Point(*args.end)).validate()

    def __repr__(self):
        attributes = [att for att in dir(self) if type(getattr(self, att)) != types.MethodType and '__' not in att]
        return ', '.join(map(lambda att: f"{att}={getattr(self, att)}", attributes))


class PipeGrid(Grid):
    """
    Representation of game's board made out of individual Fields.
    """

    def __init__(self, width, height, value, point_start, point_end):
        super().__init__(width, height, value)
        self.point_start = point_start
        self.point_end = point_end

        self.setup_pipes()

    @classmethod
    def from_preset(cls, prs: Presets):
        return cls(prs.width, prs.height, prs.base_symbol, prs.start_point, prs.end_point)

    def get_pipe_outputs(self, point: Point):
        symbol = self.get(point).symbol
        outputs = PipeType.outputs_of(symbol)

        # Get direction of pipes outputs
        outputs = map(lambda output: output + point, outputs)

        # Filter out borders
        return filter(lambda output: output in self, outputs)

    def get_possible_ways(self, point: Point):
        outputs = self.get_pipe_outputs(point)
        outputs = filter(lambda output: point in self.get_pipe_outputs(output), outputs)
        return list(outputs)

    def check_connection(self):
        return check_connection(self)

    def get_path_masked_grid(self, path):
        grid = Grid.as_grid(self, value=' ')
        for point in path:
            grid.set(point, value=self.get(point))
        return grid

    def check_solved(self):
        # TODO na pewno > 0, co jak nie znajdzie, nie zwraca kawalka sciezki?
        return len(self.check_connection()) > 0

    def setup_pipes(self):
        self.set(Point(1, 0), Pipe.by_dirs(up=True, down=True))
        self.set(Point(0, 1), Pipe.by_dirs(left=True, down=True, right=True))
        self.set(Point(3, 2), Pipe.by_dirs(left=True, up=True))
        self.set(Point(4, 1), Pipe.by_dirs(down=True, up=True))
        pass
