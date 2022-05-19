from collections import defaultdict
matrix = set()
maxX, maxY = 0, 0
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for input_line in open("input").readlines()[1:]:
    lx, ly, ux, uy = map(int, input_line.split(","))
    for x in range(lx, ux):
        if x > maxX:
            maxX = x
        for y in range(ly, uy):
            matrix.add((x, y))
            if y > maxY:
                maxY = y


def explore(x, y: int, visited: set) -> int:
    visited.add((x, y))
    size = 1
    for dir in dirs:
        tx, ty = x + dir[0], y + dir[1]
        if (tx, ty) in visited or (tx, ty) not in matrix:
            continue

        size += explore(tx, ty, visited)

    return size


def get_max_island() -> int:
    visited = set()
    max_island = 0
    for x, y in matrix:
        if (x, y) in visited:
            continue

        this_visited = set()
        island_size = explore(x, y, this_visited)
        if island_size > max_island:
            max_island = island_size

    return max_island


print(get_max_island())
