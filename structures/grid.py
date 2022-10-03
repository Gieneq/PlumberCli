from utils.point import Point
from structures.pipe import Pipe
from utils.pallet import CORRUPTED_SYMBOL

class Grid:
    def __init__(self, width, height, value=0):
        self.width = width
        self.height = height
        self.grid = [[value] * width for _ in range(height)]

    @classmethod
    def as_grid(cls, grid, value=0):
        return cls(grid.width, grid.height, value)

    def __contains__(self, point: Point):
        """
        Check whether Point is inside (right inclusive) Board.
        :param point: Point to be checked.
        :returns: bool
        """
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def get_rows(self):
        for row in self.grid:
            yield row

    def get_row(self, y: int):
        """
        Retrieve fields row as characters list.
        :param y: Row index.
        :returns: Characters list representing pipe.
        :raises IndexError: if value of y is not inside the Board's height.
        """
        if 0 <= y < self.height:
            return self.grid[y]

        raise IndexError(f"Cannot get row with y index of {y}")

    def get(self, point: Point):
        """
        Retrieve field as Field.
        :param point: Point pointing the field.
        :returns: Character representing pipe.
        :raises IndexError: if point is not inside the Board.
        """
        if point not in self:
            raise IndexError(f"Point: {point} is not proper coordinate.")

        return self.grid[point.y][point.x]

    def set(self, point: Point, value):

        if point not in self:
            raise IndexError(f"Point: {tuple(point)} is not proper coordinate.")

        self.grid[point.y][point.x] = value
        return value

    def draw_path(self, path, value='*'):
        # TODO refactor, overide method
        if value == '*':
            for point in path:
                self.set(point, value)
        elif value == Pipe:

            if len(path) > 1:
                # it is chained, front and rear are important
                for p_idx in range(len(path)-2):
                    p_idx += 1
                    diffs = path[p_idx-1] - path[p_idx], path[p_idx+1] - path[p_idx]

                    up, left, down, right = [False]*4

                    for diff in diffs:
                        if diff.x > 0:
                            right = True
                        if diff.x < 0:
                            left = True
                        if diff.y > 0:
                            up = True
                        if diff.y < 0:
                            down = True

                    symbol = Pipe.by_dirs(up=up, left=left, down=down, right=right)
                    # print(p_idx, path[p_idx], diffs, symbol, up, left, down, right)
                    self.set(path[p_idx], symbol)
                    self.set(path[0], value=CORRUPTED_SYMBOL)
                    self.set(path[-1], value=CORRUPTED_SYMBOL)



        return self

    def __str__(self):
        return ',\n'.join([str(g) for g in self.grid])

