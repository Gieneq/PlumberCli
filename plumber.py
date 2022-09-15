import argparse
from board import Point, Board
from render import Renderer

class Game:
    def __init__(self, presets:Presets):
        self.board = Board()

    def start(self):
        self.loop()

    def loop(self):
        print('abc')

game = Game()
game.start()

