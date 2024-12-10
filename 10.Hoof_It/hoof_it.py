# First find trail heads, for each trail head calculate the score
from collections import deque

def parse_input(file: any) -> list:
    return [list(map(int, list(line.strip()))) for line in file]

def out_of_bounds(x: int, y: int) -> bool:
    return x >= ROWS or x < 0 or y >= COLUMNS or y < 0

def find_score_and_rating(trailhead: tuple) -> tuple:
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    rating = 0
    queue = deque([trailhead])
    visited_ends = set()
    while queue:
        x, y = queue.popleft()
        for direction in directions:
            dx, dy = direction
            next_x, next_y = x + dx, y + dy
            if out_of_bounds(next_x, next_y): continue
            if TOPOGRAPHIC_MAP[next_x][next_y] - TOPOGRAPHIC_MAP[x][y] == 1:
                if TOPOGRAPHIC_MAP[next_x][next_y] == 9: 
                    rating += 1
                    visited_ends.add((next_x, next_y))
                else: queue.append((next_x, next_y))
    return len(visited_ends), rating

def find_trailheads() -> list:
    trailheads = list()
    for x in range(ROWS):
        for y in range(COLUMNS):
            if TOPOGRAPHIC_MAP[x][y] == 0:
                trailheads.append((x, y))
    return trailheads

def find_trailhead_score_and_rating_sum() -> tuple:
    trailheads = find_trailheads()
    total_score = total_rating = 0
    for trailhead in trailheads:
        score, rating = find_score_and_rating(trailhead)
        total_score += score
        total_rating += rating
    return total_score, total_rating

with open("./10.Hoof_It/sample_input.txt") as file:
    TOPOGRAPHIC_MAP = parse_input(file)
    ROWS, COLUMNS = len(TOPOGRAPHIC_MAP), len(TOPOGRAPHIC_MAP[0])
    print(find_trailhead_score_and_rating_sum()) # Both Part 1 and Part 2 answers returned as a tuple
    