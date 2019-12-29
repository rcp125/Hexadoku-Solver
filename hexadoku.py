import cv2

hex_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def read_board(img): # extract numbers and letters from grid
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def solve(path):
    grid = []
    with open(path, 'r') as f:
        for line in f.readlines():
            grid.append(line.split('\t'))

    res = ""

    if(fill_grid(grid,0,0) == 0):
        res = "not solvable"
        return res
    # fill_grid(0,0)

    for i in range(16):
        for j in range(16):
            res += grid[i][j] + "\t"
        res += "\n"

    return res

def fill_grid(grid, row, col):
    if(col == 16):
        row+=1
        col=0
    if(row == 16 and col == 0):
        return 1
    
    if(grid[row][col] == '-'):
        index = 0
        while(index < 16):
            if(check_row(grid, row, hex_values[index], -1) and check_col(grid, col, hex_values[index], -1) and check_subgrid(grid, row, col, hex_values[index], -1, -1)):
                grid[row][col] = hex_values[index]
                if(fill_grid(grid, row, col+1)):
                    return 1
            index+=1
        grid[row][col] = '-'
        return 0

    return fill_grid(grid, row, col + 1)


def check_row(grid, row, input_val, i2):
    for i in range(16):
        if(grid[row][i] == input_val and i != i2):
            return 0
    return 1

def check_col(grid, col, input_val, i2):
    for i in range(16):
        if(grid[i][col] == input_val and i != i2):
            return 0
    return 1

def check_subgrid(grid, row, col, input_val, i2, j2):
    startx = int(row/4) * 4
    starty = int(col/4) * 4
    for i in range(startx, startx + 4):
        for j in range(starty, starty + 4):
            if(grid[i][j] == input_val and i != i2 and j != j2):
                return 0
    return 1