from structures.grid import Grid
from utils.point import Point
from queue import Queue


class Path(list):
    pass


# TODO BFS alg


def check_connection(pipe_grid, algorithm_name='BFS') -> Path:
    point_start, point_end = pipe_grid.point_start, pipe_grid.point_end
    checking_grid = Grid.as_grid(pipe_grid, value=0)
    # print(f"Checking connection between {point_start} and {point_end}")

    def process_using_dfs(p1, p2, depth=1):
        checking_grid.set(p1, depth)

        if p1 == p2:
            # print(f'Found with depth {depth}!')
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

    def process_using_bfs(p1, p2, depth=1):
        bfs_queue = Queue()
        bfs_queue.put(p1)
        checking_grid.set(p1, depth)
        temp_path = []
        found = False

        while not bfs_queue.empty():
            # print(depth, end='')
            point = bfs_queue.get()
            temp_path.append((point, checking_grid.get(point)))
            if point == p2:
                # print('Found')
                found = True
                break
            depth = checking_grid.get(point) + 1
            neighbours = pipe_grid.get_possible_ways(point)
            for neighbour in neighbours:
                can_enter = checking_grid.get(neighbour) == 0
                if can_enter:
                    # print(neighbour, end='')
                    bfs_queue.put(neighbour)
                    checking_grid.set(neighbour, depth)
            # print()

        if not found or len(temp_path) == 0:
            return Path()

        temp_path = list(reversed(temp_path))
        point_pivot, depth_pivot = temp_path.pop(0)
        path = Path()
        path.append(point_pivot)
        # print(temp_path)

        for point, depth in temp_path:
            if depth == depth_pivot - 1:
                if point in pipe_grid.get_possible_ways(point_pivot):
                    depth_pivot -= 1
                    path.append(point)
                    point_pivot = point

        return path

    algorithm = process_using_dfs if algorithm_name == 'DFS' else process_using_bfs
    return algorithm(point_start, point_end)
