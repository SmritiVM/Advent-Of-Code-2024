def parse_input(file):
    grid = list()
    for line in file:
        grid.append(list(line.strip('\n')))
    return grid

# Part 1
def search_grid(grid, row, column, word):
    rows, columns = len(grid), len(grid[0])

    if grid[row][column] != word[0]:
        return False
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    
    word_length = len(word)
    word_count = 0

    for direction in directions:
        dx, dy = direction
        x, y = row + dx, column + dy
        index = 1

        while index < word_length:
            if x >= rows or x < 0 or y >= columns or y < 0: break
            if grid[x][y] != word[index]: break
            x += dx
            y += dy
            index += 1

        if index == word_length: # Word Found
            word_count += 1 
    return word_count
    

def count_word_occurences(grid, word):
    rows, columns = len(grid), len(grid[0])
    word_count = 0
    for row in range(rows):
        for column in range(columns):
            word_count += search_grid(grid, row, column, word)
    return word_count


# Part 2
# X-MAS. If the center letter has two diagonal words connected to it, word_count can be increased by 1
def out_of_bounds(x, y, rows, columns):
    return x >= rows or x < 0 or y >= columns or y < 0

def get_X_MAS_letter(x, y, rows, columns, grid):
    if out_of_bounds(x, y, rows, columns): return False
    letter = grid[x][y]
    if letter not in ['M', 'S']: return False
    return letter

def search_grid_X_MAS(grid, row, column):
    rows, columns = len(grid), len(grid[0])
    if grid[row][column] != 'A': return False

    directions = [(-1, -1), (-1, 1)]
    word_count = 0
    for direction in directions:
        dx, dy = direction
        first_letter = get_X_MAS_letter(row + dx, column + dy, rows, columns, grid)
        second_letter = get_X_MAS_letter(row - dx, column - dy, rows, columns, grid)

        if first_letter and second_letter and first_letter != second_letter: 
            word_count += 1
    if word_count == 2: return 1
    return False

def count_X_MAS(grid):
    rows, columns = len(grid), len(grid[0])
    word_count = 0
    for row in range(rows):
        for column in range(columns):
            word_count += search_grid_X_MAS(grid, row, column)
    return word_count


with open("./04.Ceres_Search/input.txt") as file:
    GRID = parse_input(file)
    print(count_word_occurences(GRID, 'XMAS'))
    print(count_X_MAS(GRID))