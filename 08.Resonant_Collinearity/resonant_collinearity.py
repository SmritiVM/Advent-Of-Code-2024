def parse_input(file):
    return [list(line.strip('\n')) for line in file]

def find_antennas(grid):
    rows, columns = len(grid), len(grid[0])
    antennas = []
    for x in range(rows):
        for y in range(columns):
            if grid[x][y] != '.': antennas.append((x, y))
    return antennas


def is_valid_antinode(antinode, rows, columns):
    x, y = antinode
    return x >= 0 and x < rows and y >= 0 and y < columns

def generate_antinodes(antenna, next_antenna, rows, columns, multiple):
    x1, y1 = antenna
    x2, y2 = next_antenna
    dx, dy = x1 - x2, y1 - y2
    x, y = x1 + dx, y1 + dy
    antinodes = set()
    while is_valid_antinode((x, y), rows, columns):
        antinodes.add((x, y))
        if not multiple: break
        x += dx
        y += dy
    if multiple: antinodes.add((x1, y1))
    return antinodes


def find_unique_antinodes(antennas, grid, multiple = False):
    rows, columns = len(grid), len(grid[0])
    unique_antinodes = set()
    for index, antenna in enumerate(antennas):
        for next_antenna in antennas[index + 1:]:
            if grid[antenna[0]][antenna[1]] == grid[next_antenna[0]][next_antenna[1]]:
                unique_antinodes.update(generate_antinodes(antenna, next_antenna, rows, columns, multiple))
                unique_antinodes.update(generate_antinodes(next_antenna, antenna, rows, columns, multiple))
    return len(unique_antinodes)


with open("./08.Resonant_Collinearity/input.txt") as file:
    GRID = parse_input(file)
    ANTENNAS = find_antennas(GRID)
    print(find_unique_antinodes(ANTENNAS, GRID))
    # print(find_unique_antinodes(ANTENNAS, GRID, multiple=True))


# (2, 5), (3,7)
# dx = -1, dy = -2
# 2 + dx, 5 + dy = (1, 3)
# 3 - dx, 7 - dy = (4, 9)

# (1, 8), (2, 5)
# dx = -1 dy = 3
# 1 + dx, 8 + dy = (0, 11)
# 2 - dx, 3 - dy = (3, 2)