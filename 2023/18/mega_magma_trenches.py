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


MAX_X = 0
MAX_Y = 0

with open("C:\\Users\\Nate\\Desktop\\Playdate\\advent-of-code\\2023\\18\\test.txt", "r") as file:

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

    
    horizontal_max = 0
    horizontal_min = 0
    vertical_max = 0
    vertical_min = 0

    pos_h = 0
    pos_v = 0


    #get max vertical and horizontal pos

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



    MAX_X = 1 + horizontal_max - horizontal_min
    MAX_Y = 1 + vertical_max - vertical_min

    start_x = -horizontal_min
    start_y = -vertical_min

    print(start_x)
    print(start_y)
    #starting with start pos, get all corner positions

    pos_set_h = set()
    pos_set_v = set()

    pos_v = start_y
    pos_h = start_x


    corner_positions = []
    
    corner_positions.append((start_x, start_y))

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

    


    print("printing corners")
    for corner in corner_positions:
        pass
        print(corner)
    print()

    list_h = list(pos_set_h)
    list_v = list(pos_set_v)

    list_h.sort()
    list_v.sort()

    print(list_h)
    print(list_v)


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


    print("printing walls")
    for wall in wall_positions:
        print(wall)
        pass
    print()
    print(len(wall_positions))
    print()


    #create grid of cells

    the_grid = []
    h_set = set()
    v_set = set()

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
            the_grid[v].append(cell)

    #grab each cell in row 1 and go through them until one has a top edge that is a wall, this is guarunteed to be an inside cell
    
    print("printing cell north walls")
    for i in range(len(the_grid[0])):
        cell = the_grid[0][i]
        #print(cell[Dir.up])
        if cell[Dir.up]["coords"] in wall_positions:
            print("found start cell")
            the_grid[0][i]["zone"] = "Inside"
            start_x = i
            start_y = 0
            break
    print()

    visited_cells = set()
    active_cells = []
    active_cells.append((start_x, start_y))


    inside_cells = set()
    walled_cells = set()

    traversal_order = []

    wall_positions = []

    while True:
        #get top cell from active cells
        if len(active_cells) == 0:
            break

        pos = active_cells.pop()
        traversal_order.append(pos)
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
            else:
                walled_cells.add(cell[d]["coords"])

    total = 0

    print("walled cells:")
    print(walled_cells)

    for i in range(len(the_grid)):
        line = ""
        for j in range(len(the_grid[i])):
            if (j,i) in  inside_cells:
                line += "#"
            else:
                line += "."
        print(line)

    for pos in inside_cells:
        cell = the_grid[pos[1]][pos[0]]
        #print(cell)
        #print()
        total += cell["area"]

    #find all connected edges
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

    #go through all connected edges and remove double counts
    print()
    c_edges = list(connected_edges)
    c_edges.sort()
    for con in c_edges:

        print(con)
        pos = con[0]
        cell = the_grid[pos[1]][pos[0]]
        total -= cell[h_v_from_edge(con)]

    print(len(c_edges))
    
    print()
    print(h_set)
    print(v_set)
    print()
    print(total)

    print(MAX_X * MAX_Y)            
    print(952408144115)
    print(total - 1407376496241)