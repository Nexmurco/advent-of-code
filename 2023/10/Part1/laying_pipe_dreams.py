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
            
            
            node = {"symbol": l, "pos": pos, "adjacencies":adj, "distance":None, "is_start": is_start}

            the_grid[y].append(node)

            x += 1
        y += 1
    
    #find nodes connected to S

    for row in range(0, len(the_grid)):
        for col in range(0, len(the_grid[row])):
            for a in the_grid[row][col]["adjacencies"]:
                if a == start_pos:
                    the_grid[start_pos[1]][start_pos[0]]["adjacencies"].append((col, row))

    #go through main loop and find distances

    mark_distances(the_grid, start_pos, 0)


    biggest_d = 0

    for row in range(0, len(the_grid)):
        r = ""
        for col in range(0, len(the_grid[row])):
            d = the_grid[row][col]["distance"]
            if d is not None:
                if d > biggest_d:
                    biggest_d = d
                
    
    print(biggest_d)
            