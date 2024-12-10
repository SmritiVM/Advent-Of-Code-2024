# First find trail heads, for each trail head calculate the score
from collections import deque

def parse_input(file):
    return [list(map(int, list(line.strip()))) for line in file]

def out_of_bounds(x, y):
    return x >= ROWS or x < 0 or y >= COLUMNS or y < 0

def find_score(trailhead):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    score = 0
    queue = deque([trailhead])
    visited = {trailhead,}
    while queue:
        # print(queue)
        x, y = queue.popleft()
        for direction in directions:
            dx, dy = direction
            next_x, next_y = x + dx, y + dy
            # print((next_x, next_y), end = " ")
            if out_of_bounds(next_x, next_y): continue
            if (next_x, next_y) in visited: continue
            if TOPOGRAPHIC_MAP[next_x][next_y] - TOPOGRAPHIC_MAP[x][y] == 1:
                if TOPOGRAPHIC_MAP[next_x][next_y] == 9: score += 1
                else: queue.append((next_x, next_y))
                visited.add((next_x, next_y))
        # print()
    return score

def find_trailheads():
    trailheads = list()
    for x in range(ROWS):
        for y in range(COLUMNS):
            if TOPOGRAPHIC_MAP[x][y] == 0:
                trailheads.append((x, y))
    return trailheads

def find_trailhead_score_sum():
    trailheads = find_trailheads()
    total = 0
    for trailhead in trailheads:
        total += find_score(trailhead)
        # print(find_score(trailhead))
    return total

with open("./10.Hoof_It/input.txt") as file:
    TOPOGRAPHIC_MAP = parse_input(file)
    ROWS, COLUMNS = len(TOPOGRAPHIC_MAP), len(TOPOGRAPHIC_MAP[0])
    # print(TOPOGRAPHIC_MAP)
    # print(find_score((0, 2)))
    print(find_trailhead_score_sum())
    