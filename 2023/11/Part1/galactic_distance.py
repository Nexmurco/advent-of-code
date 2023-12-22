

def space_taxi_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

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
    
    #generate new list and isnert
    empty_row = []
    for i in range(len(the_universe[0])):
        empty_row.append(".")

    for row in list(reversed(empty_rows)):
        print("empty row at " + str(row))
        the_universe.insert(row, empty_row.copy())
    print()


    #repeat process for columns
    print()

    empty_col_list = []
    for i in range(len(the_universe[0])):
        empty_col_list.append(i)
    
    for row in range(len(the_universe)):
        removal_list = []
        for col in empty_col_list:
            if the_universe[row][col] == "#":
                removal_list.append(col)
        
        #check for removals
        for removal in list(reversed(removal_list)):
            empty_col_list.remove(removal)
    
    #insert columns into remaining last columns

    for empty_col in list(reversed(empty_col_list)):
        for row in range(len(the_universe)):
            the_universe[row].insert(empty_col, ".")

    print("inserts new columns at:")
    print(empty_col_list)
    print()



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
            dist = space_taxi_dist(g1, g2)
            dist_total += dist

    print(dist_total)