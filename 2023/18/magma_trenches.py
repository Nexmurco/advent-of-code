from enum import Enum


class Dir(Enum):
    up = 1
    right = 2
    down = 3
    left = 4


letter_dir_dict = {
    "U": Dir.up,
    "R": Dir.right,
    "D": Dir.down,
    "L": Dir.left
}

def flip_zone(zone):
    if zone == "Outside":
        return "Inside"
    if zone == "Inside":
        return "Outside"
    
    return None

def symbol_corner(dir1, dir2):
    if dir1 == Dir.left:
        if dir2 == Dir.up:
            return "L"
        elif dir2 == Dir.down:
            return "F"
    elif dir1 == Dir.up:
        if dir2 == Dir.left:
            return "7"
        elif dir2 == Dir.right:
            return "F"
    elif dir1 == Dir.right:
        if dir2 == Dir.up:
            return "J"
        elif dir2 == Dir.down:
            return "7"
    elif dir1 == Dir.down:
        if dir2 == Dir.left:
            return "J"
        elif dir2 == Dir.right:
            return "L"

def symbol_edge(dir):
    if dir == Dir.down or dir == Dir.up:
        return "|"
    elif dir == Dir.left or dir == Dir.right:
        return "-"
    return None

the_grid = {}
MAX_X = 0
MAX_Y = 0

def move(pos_x, pos_y, dir):
    if dir==Dir.up:
        return (pos_x, pos_y - 1)
    elif dir==Dir.down:
        return (pos_x, pos_y + 1)
    elif dir==Dir.left:
        return (pos_x - 1, pos_y)
    elif dir==Dir.right:
        return (pos_x + 1, pos_y)

    return None

with open("C:\\Users\\Nate\\Desktop\\Playdate\\advent-of-code\\2023\\18\\input.txt", "r") as file:

    instructions = []
    input = list(file)
    for i in input:
        i = i.rstrip("\n")
        d, l, c = i.split(" ")
        instruct = {}
        instruct["dir"] = letter_dir_dict[d]
        instruct["len"] = int(l)
        instruct["rgb"] = c
        instructions.append(instruct)

    
    horizontal_max = 0
    horizontal_min = 0
    vertical_max = 0
    vertical_min = 0

    pos_h = 0
    pos_v = 0

    for i in instructions:
        if i["dir"] == Dir.up:
            pos_v -= i["len"]
        elif i["dir"] == Dir.down:
            pos_v += i["len"]
        elif i["dir"] == Dir.left:
            pos_h -= i["len"]
        elif i["dir"] == Dir.right:
            pos_h += i["len"]
        
        if pos_v < vertical_min:
            vertical_min = pos_v
        elif pos_v > vertical_max:
            vertical_max = pos_v
        
        if pos_h < horizontal_min:
            horizontal_min = pos_h
        elif pos_h > horizontal_max:
            horizontal_max = pos_h


    #create a 2d array with rows equal to vertical distance
    #each row will have cols equal to horizontal distance

    MAX_X = 1 + horizontal_max - horizontal_min
    MAX_Y = 1 + vertical_max - vertical_min

    start_x = -horizontal_min
    start_y = -vertical_min

    print(start_x)
    print(start_y)


    the_grid = []
    for i in range(MAX_Y):
        row = []
        for j in range(MAX_X):
            row.append(".")
        the_grid.append(row)


    
    pos_x = start_x
    pos_y = start_y

    for i in range(len(instructions)):
        cur = instructions[i]
        step_length = cur["len"]
        for step in range(step_length):
            
            if step == step_length - 1:
                if i == len(instructions) - 1:
                    next = instructions[0]
                else:
                    next = instructions[i+1]
                symbol = symbol_corner(cur["dir"], next["dir"])
            else:
                symbol = symbol_edge(cur["dir"])


            pos_x, pos_y = move(pos_x, pos_y, cur["dir"])
            the_grid[pos_y][pos_x] = symbol


    #lol reuse code from pipe interior question
            
    corner_first = None
    corner_last = None

    corners = ["J", "L", "7", "F"]


    for row in range(len(the_grid)):
        zone_cur = "Outside"
        for col in range(len(the_grid[row])):
            #start by having us be outside, if we hit a pipe "|" then flip. If we hit a corner wait until we see the next corner and then evaluate based on if we continue in the same vertical direction or u-turn in the oppisite vertical direciton
            char = the_grid[row][col]
            if char != ".":
                if char == "|":
                    zone_cur = flip_zone(zone_cur)
                elif char in corners:
                    if corner_first is None:
                        corner_first = char
                    elif corner_last is None:
                        corner_last = char
                        #evaluate if they flip or not
                        if corner_first == "L" and corner_last == "7" or corner_first == "F" and corner_last == "J":
                            zone_cur = flip_zone(zone_cur)
                        #reset corners
                        corner_first = None
                        corner_last = None
            elif zone_cur == "Inside":
                the_grid[row][col] = "#"
    

    fout = open("C:\\Users\\Nate\\Desktop\\Playdate\\advent-of-code\\2023\\18\\output.txt", "w")


    count = 0
    for row in the_grid:
        s = ""
        for col in row:
            s += col
            if col != ".":
                count += 1
        print(s, file=fout)

    fout.close()

    print(count)
            

