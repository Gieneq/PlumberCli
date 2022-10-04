# from enum import Enum
# from utils import Point, Presets, gen_x_coord_labels, gen_y_coord_labels


# self.x_coord_labels = gen_x_coord_labels(self.width)
# self.y_coord_labels = gen_y_coord_labels(self.height)
# print(self.x_coord_labels)
# print(self.y_coord_labels)


# def validate_coord(self, x: str, y: str):
#     return x in self.x_coord_labels and y in self.y_coord_labels

import re
from functools import reduce

from utils.point import Point


def eval_cmd(cli_line, game):
    board = game.board
    #TODO indexy zbyt na sztywno, moze wejscia A-Z nie przeskocze ale controller powinien miec x w int

    cli_line = cli_line.lower()
    cli_line = re.findall(r'[a-z][0-9]+[rl]+', cli_line)
    if len(cli_line) != 1:
        raise ValueError(f"Something weird with cmd {cli_line}.")
    cli_line = cli_line[0]

    x_search_idx = re.search(r'^[a-z]', cli_line).span()[1]
    x = ord(cli_line[:x_search_idx]) - ord('a')
    cli_line = cli_line[x_search_idx:]

    y_search_idx = re.search('^[0-9]+', cli_line).span()[1]
    y = int(cli_line[:y_search_idx]) - 1
    cli_line = cli_line[y_search_idx:]

    n_turns = int(reduce(lambda a, b: a + (1 if b == 'r' else -1), cli_line, 0))

    board.rotate_pipe(Point(x, y), n_turns)
    game.record_move()
