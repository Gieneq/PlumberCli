# from board import Board
from math import ceil

wall = '█'
wall_bottom = '▄'
wall_top = '▀'

PALLET_DEFAULT = {
    '╬': '╬',
    ' ': ' ',
    '║': '║',
    '═': '═',
    '╩': '╩',
    '╠': '╠',
    '╦': '╦',
    '╣': '╣',
    '╚': '╚',
    '╔': '╔',
    '╗': '╗',
    '╝': '╝',
}

PALLET_THIN = {
    '╬': '┼',
    ' ': ' ',
    '║': '│',
    '═': '─',
    '╩': '┴',
    '╠': '├',
    '╦': '┬',
    '╣': '┤',
    '╚': '└',
    '╔': '┌',
    '╗': '┐',
    '╝': '┘',
}

PALLET_HIDDEN = dict((k, '*') for k, _ in PALLET_DEFAULT.items()) | {' ': ' '}

CORRUPTED_SYMBOL = '?'


class Renderer:

    # TODO interface zamiast obiektu

    @staticmethod
    def render(grid, palet=PALLET_DEFAULT):
        print('Has grid?', hasattr(grid, 'get_grid'))

        x_labels_chars = ord('Z') - ord('A') + 1
        x_labels_count = grid.width
        x_labels_rows = ceil(x_labels_count / x_labels_chars) + 1
        x_labels_per_row = ceil(x_labels_count / x_labels_rows)

        y_labels_count = grid.height
        y_labels_digits = len(str(y_labels_count)) + 1
        print(x_labels_count, x_labels_per_row, x_labels_rows)

        for row_idx in range(x_labels_rows):
            labels_row = ' ' * y_labels_digits + wall + ' ' * row_idx
            for label_idx in range(x_labels_per_row):
                label_value = row_idx + label_idx * x_labels_rows
                if label_value > x_labels_count:
                    break
                label = f"{chr(label_value + ord('A')):<{x_labels_rows}}"
                labels_row += label
            labels_row = labels_row[0:x_labels_count + 3] + wall
            print(labels_row)

        print(wall_bottom * y_labels_digits + wall + wall_bottom * x_labels_count + wall)

        rows = list(grid.get_rows())
        for idx, row in enumerate(reversed(rows)):
            str_row = (str(r) for r in row)
            draw_row = [palet[sr] if sr in palet.keys() else CORRUPTED_SYMBOL for sr in str_row]
            print(f"{len(rows) - idx:>{y_labels_digits - 1}} {wall}", *draw_row, wall, sep='')

        print(wall_top * (y_labels_digits + x_labels_count + 2))
