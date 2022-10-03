from structures.grid import Grid
from utils.point import Point


class Path(list):
    pass


# TODO BFS alg

def check_connection(pipe_grid) -> Path:
    point_start, point_end = pipe_grid.point_start, pipe_grid.point_end
    checking_grid = Grid.as_grid(pipe_grid, value=0)
    print(f"Checking connection between {point_start} and {point_end}")

    def process_using_dfs(p1, p2, depth=1):
        checking_grid.set(p1, depth)

        if p1 == p2:
            print(f'Found with depth {depth}!')
            return Path([p1])

        neighbours = pipe_grid.get_possible_ways(p1)

        for neighbour in neighbours:
            can_enter = checking_grid.get(neighbour) == 0
            if can_enter:
                # print(f"From {p1} entering {neighbour}")
                tail = process_using_dfs(neighbour, p2, depth + 1)
                if len(tail) != 0:
                    # found path to the target
                    return Path([p1]) + tail
        return Path()

    return process_using_dfs(point_start, point_end)
