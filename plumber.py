import argparse
from utils import Point, Presets
from board import Board
from render import Renderer

class Game:
    def __init__(self, presets:Presets):
        self.board = Board()

    def start(self):
        self.loop()

    def loop(self):
        print('abc')


parser = argparse.ArgumentParser(description='Sth')
parser.add_argument('--width', type=int, default=8)
parser.add_argument('--height', type=int, default=8)
parser.add_argument('--start', nargs=2, type=int, default=[0, 0])
parser.add_argument('--end', nargs=2, type=int, default=[7, 7])
parser.add_argument('--difficulty', choices=['easy', 'normal', 'hard', 'mad'], default='normal')
presets = Presets.buildFromArgs(parser.parse_args())
print(presets)
game = Game(presets)
game.start()
