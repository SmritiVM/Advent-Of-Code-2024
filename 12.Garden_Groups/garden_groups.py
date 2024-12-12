from collections import deque

def parse_input(file):
    return [list(line.strip()) for line in file.readlines()]

def out_of_bounds(x: int, y: int) -> bool:
    return x >= ROWS or x < 0 or y >= COLUMNS or y < 0

def search_depth_wise(start, visited):
    stack = deque([start])
    current_group = {start, }
    while stack:
        x, y = stack.pop()
        for direction in DIRECTIONS:
            dx, dy = direction
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in visited or out_of_bounds(new_x, new_y): continue
            if GARDEN[x][y] == GARDEN[new_x][new_y]:
                visited.add((new_x, new_y))
                stack.append((new_x, new_y))  
                current_group.add((new_x, new_y))
    return visited, current_group       

def find_area_perimeter(garden_group):
    area = len(garden_group)
    perimeter = 0
    for x, y in garden_group:
        for direction in DIRECTIONS:
            dx, dy = direction
            new_x, new_y = x + dx, y + dy
            if out_of_bounds(new_x, new_y):
                perimeter += 1
                continue
            if GARDEN[x][y] != GARDEN[new_x][new_y]: perimeter += 1
    return area, perimeter

def find_fencing_price():
    visited = set()
    total_price = 0
    for x in range(ROWS):
        for y in range(COLUMNS):
            if (x, y) not in visited:
                visited, current_group= search_depth_wise((x, y), visited)
                area, perimeter = find_area_perimeter(current_group)
                total_price += area * perimeter
    return total_price


with open("./12.Garden_Groups/input.txt") as file:
    GARDEN = parse_input(file)
    ROWS, COLUMNS = len(GARDEN), len(GARDEN[0])
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    print(find_fencing_price())