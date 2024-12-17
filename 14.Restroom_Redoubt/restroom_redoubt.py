import re
from collections import defaultdict
from functools import reduce

def parse_input(file):
    robots = list()
    for line in file:
        coordinates = list(map(int, re.findall('-*\d+', line)))
        robots.append({"position":(coordinates[0], coordinates[1]), "velocity":(coordinates[2], coordinates[3])})
    return robots

def out_of_bounds(x, y):
    return x < 0 or x >= X_LIMIT or y < 0 or y >= Y_LIMIT

def move_robot(position, velocity):
    x, y = position
    vx, vy = velocity
    return (x + vx) % X_LIMIT, (y + vy) % Y_LIMIT

def simulate_robot_movement(turns):
    robot_positions = defaultdict(int)
    for robot in ROBOTS:
        position, velocity = robot["position"], robot["velocity"]
        for _ in range(turns):
            position = move_robot(position, velocity)
        robot_positions[position] += 1
    return robot_positions

def find_quadrant_wise_robots(robot_positions):
    mid_x, mid_y = X_LIMIT // 2, Y_LIMIT // 2
    quadrant = [0,0,0,0]
    for position in robot_positions:
        x, y = position
        if x == mid_x or y == mid_y: continue
        if x < mid_x and y < mid_y: quadrant[0] += robot_positions[position]
        elif x < mid_x and y > mid_y: quadrant[1] += robot_positions[position]
        elif y < mid_y : quadrant[2] += robot_positions[position]
        else: quadrant[3] += robot_positions[position]
    return quadrant

def find_safety_factor():
    robot_positions = simulate_robot_movement(100)
    quadrant = find_quadrant_wise_robots(robot_positions)
    safety_factor = reduce(lambda x, y: x * y, quadrant)
    return safety_factor

def find_unique_positions():
    turns = 1
    while True:
        robot_positions = defaultdict(int)
        for index, robot in enumerate(ROBOTS):
            position, velocity = robot["position"], robot["velocity"]
            new_position = move_robot(position, velocity)
            ROBOTS[index]["position"] = new_position
            robot_positions[new_position] += 1
        if len(robot_positions) == 500:
            break
        turns += 1
    return turns



with open("./14.Restroom_Redoubt/input.txt") as file:
    ROBOTS = parse_input(file)
    X_LIMIT, Y_LIMIT = 101, 103
    print(find_safety_factor())
    print(find_unique_positions())