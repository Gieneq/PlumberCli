from utils.point import Point
from structures.grid_pipes import PipeGrid, Presets
from structures.grid import Grid
from utils.render import Renderer
from structures.pipe import Pipe


class Game:
    def __init__(self, presets: Presets):
        self.board = PipeGrid.from_preset(presets)
        Renderer.init()

    def start(self):
        self._loop()

    def _process_input(self):
        line = input('=>')
        return -1

    def _update(self):
        pass

    def _render(self):
        Renderer.render(self.board)

    def _loop(self):
        # self._process_input()
        # self._update()
        self._render()
        path = self.board.find_connection_path()
        result_grid = Grid.as_grid(self.board, value=' ')
        result_grid.draw_path(path, value=Pipe)
        # result_grid = self.board.get_path_masked_grid(path)
        # Renderer.render(result_grid)
        # print(len(path), path, )



# parser = argparse.ArgumentParser(description='Sth')
# parser.add_argument('--width', type=int, default=8)
# parser.add_argument('--height', type=int, default=8)
# parser.add_argument('--start', nargs=2, type=int, default=[0, 0])
# parser.add_argument('--end', nargs=2, type=int, default=[7, 7])
# parser.add_argument('--difficulty', choices=['easy', 'normal', 'hard', 'mad'], default='normal')
# presets = Presets.buildFromArgs(parser.parse_args())
# print(presets)

def main():
    general_pipe = Pipe.by_dirs(up=True, left=True, down=True, right=True)
    presets = Presets().with_width(5).with_height(3).with_end_point(Point(4, 2)).with_base_symbol(general_pipe).validate()
    game = Game(presets)
    game.start()


if __name__ == "__main__":
    main()
