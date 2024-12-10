from enum import Enum

max_x = -1
max_y = -1

def add(a, b):
    val =  (a[0] + b[0], a[1] + b[1])
    return val

def is_in_bounds(pos):
    global max_x
    global max_y
    return (pos[0] >= 0 and pos[1] >= 0 and pos[0] < max_x and pos[1] < max_y)

class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

movement = {
    Dir.North: (0,-1),
    Dir.East: (1,0),
    Dir.South: (0,1),
    Dir.West: (-1,0)
}

def grid_search(pos, grid, prev_step): 

    sum = 0

    x = pos[0]
    y = pos[1]

    current_step = grid[y][x]

    if int(current_step) - int(prev_step) == 1:
        if current_step == "9":
            return 1
        else:
            for d in Dir:
                next_pos = add(pos, movement[d])
                if is_in_bounds(next_pos):
                    sum += grid_search(next_pos, grid, current_step)
                    
    
    return sum


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\10\\Input\\input.txt", "r") as file:
    
    lines = [] 
    for line in file:
        line = line.rstrip("\n")
        lines.append(line)

    max_x = len(lines[0])
    max_y = len(lines)

    sum = 0

    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            pos = (j,i)
            paths = grid_search(pos, lines, -1)
            sum += paths

    print(sum)
