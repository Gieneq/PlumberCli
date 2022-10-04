from structures.grid_pipes import PipeGrid, Presets
from utils.render import Renderer
import argparse
from utils.controller import eval_cmd


class Game:
    def __init__(self, prsts: Presets):
        print(f'Setting up game [{prsts.width} x {prsts.height}] difficulty: {prsts.difficulty}.')
        self.board = PipeGrid.from_preset(prsts)
        self.moves_count = 0
        Renderer.init()

    @staticmethod
    def shut(msg='See you!'):
        print(msg)
        exit(1)

    def record_move(self):
        self.moves_count += 1

    def start(self):
        while True:
            self._loop()

    def _process_input(self):
        try:
            line = input('=>')
            eval_cmd(line, self)
        except KeyboardInterrupt:
            Game.shut()
        return -1

    def _update(self):
        if self.board.check_solved():
            msg = f'Solved with {self.moves_count} moves!'
            Game.shut(msg)

    def _render(self):
        Renderer.render(self.board)
        print("Rotate pipes to let water flow e.g. 'A1l', 'c2rr', 'e1rlrlrl', 'h' for help, Ctrl-Z for exit.")

    def _loop(self):
        self._render()
        self._process_input()
        self._update()


def create_exec_args_parser():
    exec_parser = argparse.ArgumentParser(description='Sth')
    exec_parser.add_argument('--width', type=int, default=4)
    exec_parser.add_argument('--height', type=int, default=4)
    exec_parser.add_argument('--start', nargs=2, type=int, default=[0, 0])
    exec_parser.add_argument('--end', nargs=2, type=int, default=[3, 3])
    exec_parser.add_argument('--difficulty', choices=['easy', 'normal', 'hard', 'mad', 'random'], default='random')
    return exec_parser


def main():
    exec_parser = create_exec_args_parser()
    # test_cmd_line = ['--width', '26', '--height', '4', '--end', '3', '3']
    parsed_args = exec_parser.parse_args()
    initial_presets = Presets.build_from_args(parsed_args)
    game = Game(initial_presets)
    game.start()


if __name__ == "__main__":
    main()
