from enum import Enum

def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

def is_in_bounds(pos):
    global max_x
    global max_y
    return pos[0] < max_x and pos[0] >= 0 and pos[1] < max_y and pos[1] >= 0

class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4


arrow_movement = {
    "^": (0,-1),
    ">": (1,0),
    "v": (0,1),
    "<": (-1,0)
}

movement = {
    Dir.North: (0,-1),
    Dir.East: (1,0),
    Dir.South: (0,1),
    Dir.West: (-1,0)
}


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\15\\Input\\input.txt", "r") as file:
    lines = []
    commands = []
    pos_dict = {}
    grid = []

    max_x = -1
    max_y = -1

    input_grid = True

    for line in file:
        line = line.rstrip("\n")
        

        if line == "":
           input_grid = False 
        elif input_grid:
            row = []
            for l in line:
                row.append(l)
            grid.append(row)
        else:
            for l in line:
                commands.append(l)

    pos = (-1,-1)
    max_x = len(grid[0])
    max_y = len(grid)

    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            point = row[x]
            pos_dict[(x,y)] = point
            if point == "@":
                pos = (x,y)


    print("initial")
    for row in grid:
            string = ""
            for r in row:
                string += r
            print(string)
    print("------------")
    
    for command in commands:
        #print("command: " + str(command) + " at pos " + str(pos))
        #get the position being moved into
        direction = arrow_movement[command]
        #check if we hit a wall

        eval_move = True
        perform_move = True
        pos_move_list = []
        pos_move_list.append(pos)
        new_pos = pos

        while eval_move:
            new_pos = tuple_add(new_pos, direction)
            #print("checking pos " + str(new_pos))

            if pos_dict[new_pos] == "#":
                eval_move = False
                perform_move = False
                #print("hit wall")
            elif pos_dict[new_pos] == ".":
                eval_move = False
                perform_move = True
                #print("found open space")
            elif pos_dict[new_pos] == "O":
                pos_move_list.insert(0, new_pos)
                # print("adding position " + str(new_pos))
                # print("hit box, continuing")
        
        if perform_move:
            pos_move_list.insert(0, new_pos)
            for p in range(len(pos_move_list)):
                pos = pos_move_list[p]
                cur = pos_dict[pos]
                if (p == (len(pos_move_list) - 1)):
                    adj = "."
                else:
                    adj = pos_dict[pos_move_list[p+1]]
                
                #print("moving " + str(adj) + " into " + str(cur) + " at pos " + str(pos_move_list[p]))
                
                pos_dict[pos] = adj
                grid[pos[1]][pos[0]] = adj
            
            pos = tuple_add(pos, direction)
        
        # for row in grid:
        #     string = ""
        #     for r in row:
        #         string += r
        #     print(string)
        # print()
    

    for row in grid:
        string = ""
        for r in row:
            string += r
        print(string)
    print()
    

    sum = 0
    for pos in pos_dict:
        #print(pos)
        if pos_dict[pos] == "O":
            sum += (100 * pos[1]) + pos[0]

    print(sum)
            