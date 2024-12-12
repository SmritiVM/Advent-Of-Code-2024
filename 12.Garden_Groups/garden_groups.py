from collections import deque, defaultdict

def parse_input(file):
    return [list(line.strip()) for line in file.readlines()]

def out_of_bounds(x: int, y: int) -> bool:
    return x >= ROWS or x < 0 or y >= COLUMNS or y < 0

def search_depth_wise(start, visited):
    stack = deque([start])
    current_group = {start, }
    while stack:
        x, y = stack.pop()
        for dx, dy in DIRECTIONS:
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
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if out_of_bounds(new_x, new_y):
                perimeter += 1
                continue
            if GARDEN[x][y] != GARDEN[new_x][new_y]: 
                perimeter += 1
    return area, perimeter

# def find_boundary_points(garden_group):
#     boundary = set()
#     for x, y in garden_group:
#         for dx, dy in ALL_DIRECTIONS:
#             new_x, new_y = x + dx, y + dy
#             if out_of_bounds(new_x, new_y) or GARDEN[x][y] != GARDEN[new_x][new_y]: 
#                 boundary.add((x, y))
#     return boundary

def find_corners(garden_group):
    corners = defaultdict(lambda : 0)
    for x, y in garden_group:
        # print(x, y)
        for dx, dy in DIAGONAL_DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            # print((new_x, new_y))
            corners[(new_x, new_y)] += 1
        # print()
    return corners

def find_sides(corners, garden_group):
    sides = 0
    for corner in corners:
        if corners[corner] % 2: 
            # print(corner, corners[corner])
            sides += 1
        elif corners[corner] == 2:
            x, y = corner
            case_1 =  (x - 0.5, y - 0.5) in garden_group and (x + 0.5, y + 0.5) in garden_group
            case_2 = (x - 0.5, y + 0.5) in garden_group and (x + 0.5, y - 0.5) in garden_group
            if case_1 or case_2: 
                # print(corner, corners[corner])
                sides += 2
    # print()
    return sides

def find_fencing_price():
    visited = set()
    total_price_without_discount = total_price_with_discount = 0
    for x in range(ROWS):
        for y in range(COLUMNS):
            if (x, y) not in visited:
                visited, current_group= search_depth_wise((x, y), visited)
                area, perimeter = find_area_perimeter(current_group)
                # print(current_group)
                # print(area)
                # boundary = find_boundary_points(current_group)
                corners = find_corners(current_group)
                sides = find_sides(corners, current_group)
                # print(boundary)
                # print(corners)
                # print(sides)
                total_price_without_discount += area * perimeter
                total_price_with_discount += area * sides
    return (total_price_without_discount, total_price_with_discount)


with open("./12.Garden_Groups/input.txt") as file:
    GARDEN = parse_input(file)
    ROWS, COLUMNS = len(GARDEN), len(GARDEN[0])
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    DIAGONAL_DIRECTIONS = [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]
    ALL_DIRECTIONS = DIRECTIONS + [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # print(ALL_DIRECTIONS)
    print(find_fencing_price())