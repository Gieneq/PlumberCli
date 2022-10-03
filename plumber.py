import argparse
from utils import Point, Presets
import board
from board import Board
from render import Renderer


class Game:
    def __init__(self, presets:Presets):
        self.board = Board(presets)

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
        self.board.check_connection(self.board.start, self.board.stop)


# parser = argparse.ArgumentParser(description='Sth')
# parser.add_argument('--width', type=int, default=8)
# parser.add_argument('--height', type=int, default=8)
# parser.add_argument('--start', nargs=2, type=int, default=[0, 0])
# parser.add_argument('--end', nargs=2, type=int, default=[7, 7])
# parser.add_argument('--difficulty', choices=['easy', 'normal', 'hard', 'mad'], default='normal')
# presets = Presets.buildFromArgs(parser.parse_args())
# print(presets)

def main():
    presets = Presets().with_width(5).with_height(3).with_end_point(Point(4,2)).validate()
    game = Game(presets)
    game.start()

if __name__ == "__main__":
    main()
