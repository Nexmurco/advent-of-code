from enum import Enum

def add(a, b):
    val =  (a[0] + b[0], a[1] + b[1])
    return val

class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

rotate = {
    Dir.North: Dir.East,
    Dir.East: Dir.South,
    Dir.South: Dir.West,
    Dir.West: Dir.North
}

movement = {
    Dir.North: (0,-1),
    Dir.East: (1,0),
    Dir.South: (0,1),
    Dir.West: (-1,0)
}

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\06\\Input\\input.txt", "r") as file:
    sum = 0
    blocks = []
    pos = (-1, -1)
    
    facing = None

    lines = []
    for line in file:
        lines.append(line.rstrip("\n"))
    
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            pos_cur = (x,y)
            if line[x] == "#":
                blocks.append(pos_cur)
            elif line[x] == "^":
                facing = Dir.North
                pos = pos_cur
            elif line[x] == ">":
                facing = Dir.East
                pos = pos_cur
            elif line[x] == "v":
                facing = Dir.South
                pos = pos_cur
            elif line[x] == "<":
                facing = Dir.West
                pos = pos_cur

        max_x = len(lines[0])
        max_y = len(lines)

    run = True
    visited_pos = set(())
    print(blocks)

    while run:
        visited_pos.add(pos)
        print(str(pos) + " " + str(facing))

        new_pos = add(pos, movement[facing])

        if new_pos in blocks:
            facing = rotate[facing]
        else:
            pos = new_pos

        if new_pos[0] < 0 or new_pos[0] > max_x or new_pos[1] < 0 or new_pos[1] > max_y:
            run = False

    print()
    print(len(visited_pos)) 