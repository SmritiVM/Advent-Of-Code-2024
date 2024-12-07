def parse_input(file):
    grid = [list(line.strip('\n')) for line in file]
    return grid

def find_start(grid):
    rows, columns = len(grid), len(grid[0])
    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == '^':
                return (x, y)

def is_out_of_bounds(x, y, rows, columns):
    return x >= rows or x < 0 or y >= columns or y < 0

# Part 1
def find_distinct_visits(grid, start):
    rows, columns = len(grid), len(grid[0])
    places_visited = {start,}
    x, y = start
    direction = (-1, 0) #up
    turn_right = {(-1, 0):(0, 1), (1, 0):(0, -1), (0, -1):(-1, 0), (0, 1): (1, 0)}
    # up -> right, down -> left, left -> up, right -> down

    x, y = x + direction[0], y + direction[1]
    while not is_out_of_bounds(x, y, rows, columns):
        if grid[x][y] == '.':
            places_visited.add((x, y)) # Add to places visited
        elif grid[x][y] == '#':
            # First backtrack, then change direction
            x, y = x - direction[0], y - direction[1]  
            direction = turn_right[direction]
        x, y = x + direction[0], y + direction[1]
    return len(places_visited)

# Part 2
def check_for_loop(grid, obstacle, start, rows, columns):
    x, y = start
    direction = (-1, 0) #up
    visited = set()
    turn_right = {(-1, 0):(0, 1), (1, 0):(0, -1), (0, -1):(-1, 0), (0, 1): (1, 0)}
    x, y = x + direction[0], y + direction[1]
    # while not is_out_of_bounds(x, y, rows, columns):
    #     if grid[x][y] == '#' or (x, y) == obstacle:
    #         # First backtrack, then change direction
    #         x, y = x - direction[0], y - direction[1]  
    #         direction = turn_right[direction]
    #     elif grid[x][y] == '.':
    #         if ((x, y), direction) in path_taken:
    #             return True
    #         path_taken.append(((x, y), direction))
    #     x, y = x + direction[0], y + direction[1]
    # # print(path_taken)
    # return False 
    while True:
        if is_out_of_bounds(x, y, rows, columns):
            return False
        if grid[x][y] == '#' or (x, y) == (obstacle):
            x, y = x - direction[0], y - direction[1]  
            direction = turn_right[direction]
        elif ((x, y), direction) in visited:
            return True
        else:
            visited.add(((x, y), direction))
            x, y = x + direction[0], y + direction[1]

def find_obstruction_points(grid, start):
    possible_obstruction_points = 0
    rows, columns = len(grid), len(grid[0])
    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == '.':
                if check_for_loop(grid, (x, y), start, rows, columns): 
                    possible_obstruction_points += 1
    return possible_obstruction_points  


with open("./06.Guard_Gallivant/input.txt") as file:
    GRID = parse_input(file)
    START = find_start(GRID)
    # print(find_distinct_visits(GRID, START))
    print(find_obstruction_points(GRID, START))
    