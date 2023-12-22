

def space_taxi_dist(pos1, pos2, expanded_rows, expanded_cols, expanded_dist):
    upper = max(pos1[1], pos2[1])
    lower = min(pos1[1], pos2[1])

    right = max(pos1[0], pos2[0])
    left = min(pos1[0], pos2[0])

    #find the number of expanded rows traversed
    #row represents height (y)

    count_row = 0
    for r in expanded_rows:
        if r > lower and r < upper:
            count_row += 1

    count_col = 0
    for c in expanded_cols:
        if c > left and c < right:
            count_col += 1

    

    #find the number of expanded cols traversed
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + ((expanded_dist-1) * (count_col + count_row))

with open("D:\\Code\\Advent of Code 2023\\Dec11\\Part1\\input.txt", "r") as file:
    lines = list(file)
    the_universe = []
    for line in lines:
        line = line.rstrip("\n")
        the_universe.append(list(line))

    #check every row for gaps and then insert an extra row

    empty_rows = []
    for i in range(len(the_universe)):
        if '#' not in the_universe[i]:
            empty_rows.append(i)


    empty_cols = []
    for i in range(len(the_universe[0])):
        empty_cols.append(i)
    
    for row in range(len(the_universe)):
        removal_list = []
        for col in empty_cols:
            if the_universe[row][col] == "#":
                removal_list.append(col)
        
        #check for removals
        for removal in list(reversed(removal_list)):
            empty_cols.remove(removal)


    print(empty_rows)
    print(empty_cols)

    #sweep through universe and get position of all galaxies
    galaxy_positions = []

    for row in range(len(the_universe)):
        for col in range(len(the_universe[0])):
            if the_universe[row][col] == '#':
                galaxy_positions.append((col, row))
    
    dist_total = 0

    for i in range(len(galaxy_positions)):
        g1 = galaxy_positions[i]
        for j in range(i, len(galaxy_positions)):
            if i == j:
                continue

            g2 = galaxy_positions[j]
            dist = space_taxi_dist(g1, g2, empty_rows, empty_cols, 1000000)
            dist_total += dist

    print(dist_total)