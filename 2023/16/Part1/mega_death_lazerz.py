from enum import Enum

class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

MAX_X = 0
MAX_Y = 0

def redirect(direction, mirror):
    directions = []
    if direction == Dir.North:
        if mirror == "\\":
            directions.append(Dir.West)
        elif mirror == "/":
            directions.append(Dir.East)
        elif mirror == "-":
            directions.append(Dir.East)
            directions.append(Dir.West)
        elif mirror == "|":
            directions.append(Dir.North)
    elif direction == Dir.East:
        if mirror == "\\":
            directions.append(Dir.South)
        elif mirror == "/":
            directions.append(Dir.North)
        elif mirror == "-":
            directions.append(Dir.East)
        elif mirror == "|":
            directions.append(Dir.North)
            directions.append(Dir.South)
    if direction == Dir.South:
        if mirror == "\\":
            directions.append(Dir.East)
        elif mirror == "/":
            directions.append(Dir.West)
        elif mirror == "-":
            directions.append(Dir.East)
            directions.append(Dir.West)
        elif mirror == "|":
            directions.append(Dir.South)
    if direction == Dir.West:
        if mirror == "\\":
            directions.append(Dir.North)
        elif mirror == "/":
            directions.append(Dir.South)
        elif mirror == "-":
            directions.append(Dir.West)
        elif mirror == "|":
            directions.append(Dir.North)
            directions.append(Dir.South)

    return directions

def move(pos, direction):
    if direction == Dir.North and pos[1] > 0:
        return (pos[0], pos[1] - 1)
    elif direction == Dir.East and pos[0] < MAX_X:
        return (pos[0] + 1, pos[1])
    elif direction == Dir.South and pos[1] < MAX_Y:
        return (pos[0], pos[1] + 1)
    elif direction == Dir.West and pos[0] > 0:
        return (pos[0] - 1, pos[1]) 
    return None

mirror_char_set = {"/", "\\", "|", "-"}

with open("C:\\Users\\Nate\\Desktop\\Playdate\\advent-of-code\\2023\\16\\Part1\\input.txt", "r") as file:

    the_grid = list(file)
    mirror_map = {}
    for row in range(len(the_grid)):
        the_grid[row] = the_grid[row].rstrip("\n")
        for col in range(len(the_grid[row])):
            char = the_grid[row][col]
            pos = (col, row)
            if char in mirror_char_set:
                mirror_map[pos] = char

    MAX_X = len(the_grid[0]) - 1
    MAX_Y = len(the_grid) - 1

    laser_list = []
    
    pos = (-1,0)
    dir = Dir.East

    active_lasers = []
    active_lasers.append((pos, dir))

    while len(active_lasers) > 0:
        #get top laser
        pos, dir = active_lasers.pop(0)

        #check if we have been here before, if not, add it to the list of laser vectors
        if (pos, dir) in laser_list:
            continue
        else:
            if pos[0] != -1:
                laser_list.append((pos, dir))
        
        #move
        pos = move(pos, dir)

        #check if we have left the grid
        if pos is None:
            continue

        #check if we have collided with a mirror
        if pos in mirror_map.keys():
                #split the laser
            for d in redirect(dir, mirror_map[pos]):
                active_lasers.append((pos, d))
        else:
            active_lasers.append((pos, dir))

    energeized_positions = set()

    for l in laser_list:
        energeized_positions.add(l[0])

    print(len(energeized_positions))

        