from math import ceil
from .pallet import PALLET_DEFAULT, CORRUPTED_SYMBOL, WALL, WALL_TOP, WALL_BOTTOM

class Renderer:
    @staticmethod
    def render(grid, pallet=PALLET_DEFAULT):
        print('Has grid?', hasattr(grid, 'get_grid'))

        x_labels_chars = ord('Z') - ord('A') + 1
        x_labels_count = grid.width
        x_labels_rows = ceil(x_labels_count / x_labels_chars) + 1
        x_labels_per_row = ceil(x_labels_count / x_labels_rows)

        y_labels_count = grid.height
        y_labels_digits = len(str(y_labels_count)) + 1
        print(x_labels_count, x_labels_per_row, x_labels_rows)

        for row_idx in range(x_labels_rows):
            labels_row = ' ' * y_labels_digits + WALL + ' ' * row_idx
            for label_idx in range(x_labels_per_row):
                label_value = row_idx + label_idx * x_labels_rows
                if label_value > x_labels_count:
                    break
                label = f"{chr(label_value + ord('A')):<{x_labels_rows}}"
                labels_row += label
            labels_row = labels_row[0:x_labels_count + 3] + WALL
            print(labels_row)

        print(WALL_BOTTOM * y_labels_digits + WALL + WALL_BOTTOM * x_labels_count + WALL)

        rows = list(grid.get_rows())
        for idx, row in enumerate(reversed(rows)):
            str_row = (str(r) for r in row)
            draw_row = [pallet[sr] if sr in pallet.keys() else CORRUPTED_SYMBOL for sr in str_row]
            print(f"{len(rows) - idx:>{y_labels_digits - 1}} {WALL}", *draw_row, WALL, sep='')

        print(WALL_TOP * (y_labels_digits + x_labels_count + 2))
