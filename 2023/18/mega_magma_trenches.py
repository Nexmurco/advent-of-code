from enum import Enum


def h_v_from_edge(edge):
    c1 = edge[0]
    c2 = edge[1]

    if c2[0] - c1[0] != 0:
        return "v"
    else:
        return "h"

def split_intervals(inte, vals):
    intervals = []
    pos_initial = None
    pos_final = None
    prev_pos = None
    cur_pos = None
    for pos in vals:
        if pos > inte[0] and pos < inte[1]:
            prev_pos = cur_pos
            cur_pos = pos
            if prev_pos is None:
                pos_initial = cur_pos
            else:
                intervals.append((cur_pos, prev_pos))
                intervals.append((prev_pos, cur_pos))
        
        elif pos >= inte[1]:
            pos_final = cur_pos
            break

    if pos_initial is not None:
        intervals.append((inte[0], pos_initial))
        intervals.append((pos_initial, inte[0]))

    if pos_final is not None:
        intervals.append((pos_final, inte[1]))
        intervals.append((inte[1], pos_final))

    if len(intervals) == 0:
        intervals.append((inte[0], inte[1]))
        intervals.append((inte[1], inte[0]))
    pass
    return intervals


def flip_zone(zone):
    if zone == "Outside":
        return "Inside"
    if zone == "Inside":
        return "Outside"
    
    return None

def move(pos, dir, max_x, max_y):
    if dir == Dir.up and pos[1] > 0:
        return (pos[0], pos[1] - 1)
    elif dir == Dir.right and pos[0] < max_x:
        return (pos[0] + 1, pos[1])
    elif dir == Dir.down and pos[1] < max_y:
        return (pos[0], pos[1] + 1)
    elif dir == Dir.left and pos[0] > 0:
        return (pos[0] - 1, pos[1])
    
    return None

class Dir(Enum):
    up = 1
    right = 2
    down = 3
    left = 4


num_dir_dict = {
    0: Dir.right,
    1: Dir.down,
    2: Dir.left,
    3: Dir.up
}

letter_dir_dict = {
    "U": Dir.up,
    "R": Dir.right,
    "D": Dir.down,
    "L": Dir.left
}

def max_x_y(instructions):

    pos_h = 0
    pos_v = 0

        
    horizontal_max = 0
    horizontal_min = 0
    vertical_max = 0
    vertical_min = 0

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



    return (horizontal_max - horizontal_min, vertical_max - vertical_min, -horizontal_min, -vertical_min)
    
def get_corners(instructions, x, y):
    pos_v = y
    pos_h = x
    corner_positions = []
    corner_positions.append((x, y))

    pos_set_h = set()
    pos_set_v = set()

    for i in instructions:

        if i["dir"] == Dir.up:
            pos_v -= i["len"]
        elif i["dir"] == Dir.down:
            pos_v += i["len"]
        elif i["dir"] == Dir.left:
            pos_h -= i["len"]
        elif i["dir"] == Dir.right:
            pos_h += i["len"]
        
        pos_set_h.add(pos_h)
        pos_set_v.add(pos_v)
        corner_positions.append((pos_h, pos_v))
    return (corner_positions, pos_set_h, pos_set_v)

def get_walls(corner_positions):
    wall_positions = []
    for i in range(len(corner_positions) - 1):
        
        int_h = (corner_positions[i][0], corner_positions[i+1][0])
        int_v = (corner_positions[i][1], corner_positions[i+1][1])


        if int_h[0] > int_h[1]:
            int_h = (int_h[1], int_h[0])
        
        if int_v[0] > int_v[1]:
            int_v = (int_v[1], int_v[0])


        intervals = []
        if int_h[0] != int_h[1]:
            intervals += split_intervals(int_h, list_h)
            pass
            for interval in intervals:
                wall_positions.append(((interval[0], int_v[0]), (interval[1], int_v[1])))
                
        elif int_v[0] != int_v[1]:
            intervals += split_intervals(int_v, list_v)
            pass
            for interval in intervals:
                wall_positions.append(((int_h[0], interval[0]), (int_h[1], interval[1])))
    
    return wall_positions

def get_grid(list_h, list_v):
    the_grid = []
    h_set = set()
    v_set = set()
    
    sum = 0
    for v in range(len(list_v) - 1):
        the_grid.append([])
        for h in range(len(list_h) - 1):
            top = list_v[v]
            bottom = list_v[v+1]
            left = list_h[h]
            right = list_h[h+1]
            cell = {}
            cell[Dir.up] = {"coords":((left, top),(right,top)), "traversed":False}
            cell[Dir.right] = {"coords":((right,top), (right,bottom)), "traversed":False}
            cell[Dir.down] = {"coords":((left,bottom), (right, bottom)), "traversed":False}
            cell[Dir.left] = {"coords":((left,top), (left,bottom)), "traversed":False}
            cell["zone"] = "Outside"
            cell["pos"] = (h,v)
            cell["h"] = 1+right - left
            h_set.add(1+right - left)
            cell["v"] = 1+bottom - top
            v_set.add(1+bottom - top)
            cell["area"] = cell["h"] * cell["v"]
            sum += cell["area"]
            #print("(" + str(h) + "," + str(v) + "): " + str(cell["area"]))
            the_grid[v].append(cell)
    #print(sum)
    return (the_grid, h_set, v_set)

def get_start_cell(the_grid, wall_positions):
    for i in range(len(the_grid[0])):
        cell = the_grid[0][i]
        #print(cell[Dir.up])
        if cell[Dir.up]["coords"] in wall_positions:
            #print("found start cell at " + str(cell["pos"]))
            the_grid[0][i]["zone"] = "Inside"
            start_x = i
            start_y = 0
            break
    return(start_x, start_y)

def get_network(the_grid, start_x, start_y):

    visited_cells = set()
    active_cells = []
    active_cells.append((start_x, start_y))
    inside_cells = set()

    the_grid[start_y][start_x]["zone"] = "Inside"

    while True:
    #get top cell from active cells
        if len(active_cells) == 0:
            break

        pos = active_cells.pop()
        inside_cells.add(pos)
        cell = the_grid[pos[1]][pos[0]]
        #add active cell to visited cells
        visited_cells.add((cell["pos"]))
        #add adjacent cells to active cells if they are unvisited and there is not a wall separating the cells
        for d in Dir:
            adj_pos = move(pos, d, len(the_grid[0])-1, len(the_grid)-1)
            collision = cell[d]["coords"] in wall_positions
            if not collision:
                if adj_pos is not None and adj_pos not in visited_cells and adj_pos not in active_cells:
                    #set cell as active and switch zone to inside
                    active_cells.append(adj_pos)
                    cell[d]["traversed"] = True
                    the_grid[adj_pos[1]][adj_pos[0]]["zone"] = "Inside"
    
    return inside_cells

def get_connections(the_grid, ):
    connected_edges = set()
    for i in range(len(the_grid)):
        for j in range(len(the_grid[i])):
            cell = the_grid[i][j]
            if cell["zone"] == "Inside":
                for d in Dir:
                    pos = (j,i)
                    adj = move(pos, d, len(the_grid[i])-1, len(the_grid)-1)
                    
                    if adj is not None and the_grid[adj[1]][adj[0]]["zone"] == "Inside":
                        if pos[0] < adj[0]:
                            n1 = pos
                            n2 = adj
                        elif adj[0] < pos[0]:
                            n1 = adj
                            n2 = pos
                        else: 
                            if pos[1] <= adj[1]:
                                n1 = pos
                                n2 = adj
                            else:
                                n1 = adj
                                n2 = pos
                    
                        connected_edges.add((n1, n2))
    return connected_edges


MAX_X = 0
MAX_Y = 0

with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\18\\input.txt", "r") as file:

    instructions = []
    input = list(file)
    for i in input:
        i = i.rstrip("\n")
        d, l, c = i.split(" ")
        instruct = {}
        c = c.replace("(", "").replace(")", "").replace("#", "")
        l, d = c[:-1], c[-1]

        d = int(d)
        l = int(l, 16)
        d = num_dir_dict[d]
        #print(str(d) + ": " + str(l))
        instruct["dir"] = d
        instruct["len"] = int(l)
        instructions.append(instruct)
    #get max vertical and horizontal pos
    MAX_X, MAX_Y, start_x, start_y = max_x_y(instructions)
    #print(start_x)
    #print(start_y)
    #starting with start pos, get all corner positions
    pos_set_h = set()
    pos_set_v = set()
    pos_v = start_y
    pos_h = start_x
    #find all corners
    corner_positions, pos_set_h, pos_set_v = get_corners(instructions,start_x,start_y)
    list_h = list(pos_set_h)
    list_v = list(pos_set_v)
    list_h.sort()
    list_v.sort()
    print("horizontal positions: ")
    print(list_h)
    print("vertical positions: ")
    print(list_v)
    wall_positions = get_walls(corner_positions)

    #comment this out to work properly
    #wall_positions = []

    print()
    print("number of walls: " + str(len(wall_positions)))
    print()
    #create grid of cells
    print("generating grid")
    the_grid, h_set, v_set = get_grid(list_h, list_v)
    print("size of grid: " + str((len(h_set), len(v_set))))
    #grab each cell in row 1 and go through them until one has a top edge that is a wall, this is guarunteed to be an inside cell
    print("finding cell north wall")
    
    #flip the comments to work
    start_x, start_y = get_start_cell(the_grid, wall_positions)
    #start_x, start_y = (0,0)
    print("starting traversal at: " + str((start_x, start_y)))
    
    print("traversing grid")
    inside_cells = get_network(the_grid, start_x, start_y)
    total = 0
    #print("finding walled cells")
    #debug
    # for i in range(len(the_grid)):
    #     line = ""
    #     for j in range(len(the_grid[i])):
    #         if (j,i) in  inside_cells:
    #             line += "#"
    #         else:
    #             line += "."
    # print(line)
    print("calculating oversized area")
    for pos in inside_cells:
        cell = the_grid[pos[1]][pos[0]]
        total += cell["area"]
        #print(str(cell["pos"]) + ": " + str(cell["area"]))
    print("total: " + str(total))
    #find all connected edges
    print("finding all edges")
    #go through all connected edges and remove double counts
    c_edges = list(get_connections(the_grid))
    c_edges.sort()
    
    print("removing duplicate wall counts")
    for con in c_edges:
        pos = con[0]
        cell = the_grid[pos[1]][pos[0]]
        orth = h_v_from_edge(con)
        total -= cell[orth]
        #print(str(con) + " - " + str(cell[orth]) + " = " + str(total))
    print("total")
    print(total)

    print("re-adding overremoved corners")
    double_corners = set()
    used_c = []
    for con in c_edges:
        if con[0][0] == con[1][0]:
            con2 = ((con[0][0]-1, con[0][1]),(con[1][0]-1, con[1][1]))
        elif con[0][1] == con[1][1]:
            con2 = ((con[0][0], con[0][1]-1),(con[1][0], con[1][1]-1))
        if (con2 in used_c):
            double_corners.add(con[1])
        used_c.append(con)

    corners = list(double_corners)
    corners.sort()

    for c in corners:
        total += 1
        #print(str(c) + " + 1 = " + str(total))
    
    print(total)


    #print(h_set)
    #print(v_set)
