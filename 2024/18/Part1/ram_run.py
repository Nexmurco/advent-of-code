from enum import Enum
from copy import copy

def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

def is_in_bounds(pos):
    global max_x
    global max_y
    return pos[0] < max_x and pos[0] >= 0 and pos[1] < max_y and pos[1] >= 0

class Dir(Enum):
    South = 1
    East = 2
    West = 3
    North = 4

movement = {
    Dir.North: (0,-1),
    Dir.East: (1,0),
    Dir.South: (0,1),
    Dir.West: (-1,0)
}

def navigate(pos, visited, depth):
    global invalid_set
    global pos_f
    global found_path_length


    # print()
    # print("pos: " + str(pos))
    # print("depth: " + str(depth))


    if pos in invalid_set:
        # print("invalid position")
        return None
    elif pos in visited:
        # print("visited position")
        return None
    elif not is_in_bounds(pos):
        # print("out of bounds")
        return None 
    elif depth >= max_depth:
        # print("max depth reached")
        return None

    visited = copy(visited)
    visited.append(pos)

    if found_path_length is not None and found_path_length < len(visited):
        # print("path exceeds length of best path")
        return None

    # print("visited: ")
    # print(visited)

    if pos == pos_f:
        found_path_length = len(visited)
        return visited

    return_path = None

    for d in Dir:
        new_pos = tuple_add(pos, movement[d])
        path = navigate(new_pos, visited, depth + 1)
        if path is not None and pos_f in path:
            if return_path is None or len(path) < len(return_path):
                return_path = path
    
    return return_path


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\18\\Input\\input.txt", "r") as file:
    grid = []
    invalid_set = set(())
    found_path_length = None
    
    max_x = 71
    max_y = 71
    max_bytes = 1024
    max_depth = 200
    
    count = 0
    for line in file:
        count += 1

        line = line.rstrip("\n")
        coords = line.split(",")
        pos = (int(coords[0]), int(coords[1]))
        invalid_set.add(pos)

        if count >= max_bytes:
            break


    for y in range(max_y):
        row = []
        string = ""
        for x in range(max_x):
            if (x,y) in invalid_set:
                char = "#"
            else:
                char = "."
            
            row.append(char)
            string += char
        grid.append(row)
        print(string)

    pos_i = (0,0)
    pos_f = (max_x-1, max_y-1)

    path = navigate(pos_i, [], 0)


    print()
    print("found path: ")
    print(path)
    print("steps: ")
    print(len(path))