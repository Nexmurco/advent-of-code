from enum import Enum
import copy

def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

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

def get_direction(pos_prev, pos_curr):
    if pos_curr[0] - pos_prev[0] > 0:
        return Dir.East
    elif pos_curr[0] - pos_prev[0] < 0:
        return Dir.West
    elif pos_curr[1] - pos_prev[1] > 0:
        return Dir.South
    elif pos_curr[1] - pos_prev[1] < 0:
        return Dir.North   
    return None

def navigate(position, direction, visited):
    global grid
    global walls

    visited = copy.copy(visited)
    visited.add(position)
    
    if position in walls:
        return None
    if position in visited:
        return None

    path = []
    path.append(position)

    for d in Dir:
        move = movement[d]
        new_pos = tuple_add(position, move)
        



with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\16\\Input\\input_test.txt", "r") as file:
    grid = []
    pos_start = (-1,-1)
    pos_end = (-1,-1)

    facing = Dir.East

    walls = set(())

    for line in file:
        line = line.rstrip("\n")
        row = []
        for l in line:
            row.append(l)
        grid.append(row)
    
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            char = row[x]
            if char == "S":
                pos_start = (x,y)
            elif char == "E":
                pos_end = (x,y)
            elif char == "#":
                walls.add((x,y))

    v = set(())
    
    navigate(pos_start, facing, v)
    
