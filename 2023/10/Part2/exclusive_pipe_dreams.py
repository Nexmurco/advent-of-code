def flip_zone(zone):
    if zone == "Outside":
        return "Inside"
    if zone == "Inside":
        return "Outside"
    
    return None

def adjacenciesFromChar(char, pos):
    if char == "|":
        return [(pos[0], pos[1]-1), (pos[0], pos[1]+1)]
    elif char == "-":
        return [(pos[0]-1, pos[1]), (pos[0]+1, pos[1])]
    elif char == ".":
        return []
    elif char == "J":
        return [(pos[0]-1, pos[1]), (pos[0], pos[1]-1)]
    elif char == "L":
        return [(pos[0]+1, pos[1]), (pos[0], pos[1]-1)]
    elif char == "7":
        return [(pos[0]-1, pos[1]), (pos[0], pos[1]+1)]
    elif char == "F":
        return [(pos[0]+1, pos[1]), (pos[0], pos[1]+1)]
    elif char == "S":
        return []
    
def mark_distances(grid, pos, dist):
    
    pos_prev = pos
    pos_cur = pos
    terminate = False

    #store direction 1 and direction 2
    grid[pos_cur[1]][pos_cur[0]]["distance"] = dist
    a1 = grid[pos_cur[1]][pos_cur[0]]["adjacencies"][0]
    a2 = grid[pos_cur[1]][pos_cur[0]]["adjacencies"][1]

    pos_cur = a1

    while not terminate:
        dist += 1
        pos_d = grid[pos_cur[1]][pos_cur[0]]["distance"]
        if pos_d == None or pos_d > dist:
            grid[pos_cur[1]][pos_cur[0]]["distance"] = dist
            aList = grid[pos_cur[1]][pos_cur[0]]["adjacencies"]
            for a in aList:
                if a != pos_prev:
                    pos_prev = pos_cur
                    pos_cur = a
                    break
                    
        else:
            terminate = True

    pos_prev = pos
    pos_cur = a2
    terminate = False
    dist = 0

    while not terminate:
        dist += 1
        pos_d = grid[pos_cur[1]][pos_cur[0]]["distance"]
        if pos_d == None or pos_d > dist:
            grid[pos_cur[1]][pos_cur[0]]["distance"] = dist
            aList = grid[pos_cur[1]][pos_cur[0]]["adjacencies"]
            for a in aList:
                if a != pos_prev:
                    pos_prev = pos_cur
                    pos_cur = a
                    break
                    
        else:
            terminate = True

def extract_node_char(node_data):
    adj_up = False
    adj_down = False
    adj_left = False
    adj_right = False

    node_pos = node_data["pos"]

    for a in node_data["adjacencies"]:
        if a[0] - node_pos[0] > 0:
            adj_right = True
        if a[0] - node_pos[0] < 0:
            adj_left = True
        if a[1] - node_pos[1] > 0:
            adj_down = True
        if a[1] - node_pos[1] < 0:
            adj_up = True

    if adj_up and adj_right:
        return "L"
    elif adj_up and adj_left:
        return "J"
    elif adj_down and adj_right:
        return "F"
    elif adj_down and adj_left:
        return "7"
    elif adj_down and adj_up:
        return "|"
    elif adj_left and adj_right:
        return "-"

with open("D:\\Code\\Advent of Code 2023\\Dec10\\Part1\\input.txt", "r") as file:
    lines = list(file)
    the_grid = []
    y = 0
    start_pos = None
    for line in lines:
        line = line.rstrip("\n")
        x = 0
        the_grid.append([])
        for l in line:
            pos = (x,y)
            is_start = False
            adj = adjacenciesFromChar(l, pos)
            if l == "S":
                start_pos = pos
                is_start = True
            
            
            node = {"zone":None ,"symbol": l, "pos": pos, "adjacencies":adj, "distance":None, "is_start": is_start}

            the_grid[y].append(node)

            x += 1
        y += 1
    
    #find nodes connected to S

    edge_set = set()

    for row in range(0, len(the_grid)):
        for col in range(0, len(the_grid[row])):
            for a in the_grid[row][col]["adjacencies"]:
                if a == start_pos:
                    the_grid[start_pos[1]][start_pos[0]]["adjacencies"].append((col, row))
    

    #loop through pipe loop and add all the posiitons to our edge set
    terminate = False

    pos_cur = start_pos
    prev_pos = start_pos

    while not terminate:
        edge_set.add(pos_cur)

        #get next position
        for a in the_grid[pos_cur[1]][pos_cur[0]]["adjacencies"]:
            if a != prev_pos:
                prev_pos = pos_cur
                pos_cur = a
                break
        
        if pos_cur == start_pos:
            terminate = True
        #if next position is the start position, end

    #convert our start space into its character equivelent
    start_char = extract_node_char(the_grid[start_pos[1]][start_pos[0]])
    the_grid[start_pos[1]][start_pos[0]]["symbol"] = start_char





    #go through main loop and find distances

    #mark_distances(the_grid, start_pos, 0)


    #loop through each row, keep track of if we are inside or outside and mark the zone

    corner_first = None
    corner_last = None

    corners = ["J", "L", "7", "F"]

    for e in edge_set:
        the_grid[e[1]][e[0]]["zone"] = "Edge"

    for row in range(0, len(the_grid)):
        zone_cur = "Outside"
        for col in range(0, len(the_grid[row])):
            #start by having us be outside, if we hit a pipe "|" then flip. If we hit a corner wait until we see the next corner and then evaluate based on if we continue in the same vertical direction or u-turn in the oppisite vertical direciton
            node = the_grid[row][col]
            if node["pos"] in edge_set:
                if node["symbol"] == "|":
                    zone_cur = flip_zone(zone_cur)
                elif node["symbol"] in corners:
                    if corner_first is None:
                        corner_first = node["symbol"]
                    elif corner_last is None:
                        corner_last = node["symbol"]
                        #evaluate if they flip or not
                        if corner_first == "L" and corner_last == "7" or corner_first == "F" and corner_last == "J":
                            zone_cur = flip_zone(zone_cur)
                        #reset corners
                        corner_first = None
                        corner_last = None
            else:
                node["zone"] = zone_cur
    

    #now all positions are marked, sum up the  interior
    inside_count = 0
    for row in range(0, len(the_grid)):
        r = ""
        for col in range(0, len(the_grid[row])):
            node = the_grid[row][col]
            if node["zone"] == "Inside":
                inside_count += 1
            r += node["zone"][0]
        #print(r)
    
    print(inside_count)