def difference_count(s1, s2):
    char_count = min(len(s1), len(s2))
    differences = 0
    for i in range(char_count):
        if s1[i] != s2[i]:
            differences += 1
    
    return differences

with open("D:\\Code\\Advent of Code 2023\\Dec13\\Part2\\input.txt", "r") as file:
    lines = list(file)
    zones = []
    zone_rows = []
    
    for line in lines:
        line = line.rstrip("\n")
        if line == "":
            zones.append(zone_rows.copy())
            zone_rows = []
        else:
            zone_rows.append(line)

    # for z in zones:
    #     for r in z:
    #         print(r)
    #     print()

    total = 0

    for z in range(len(zones)):
        zone = zones[z]
        #try first by row
        r_prev = None
        is_match = False
        for i in range(len(zone)):
            offset = 0
            is_match = False
            diff_count = 0
            while True:
                if (i+offset) >= len(zone) or ((i-1) - offset) < 0:
                    break

                is_match = True
                l_1 = zone[i+offset]
                l_2 = zone[(i-1)-offset]

                diff_count += difference_count(l_1, l_2)

                if diff_count > 1:
                    is_match = False
                    break
                offset += 1

            if is_match and diff_count == 1:
                break

        if is_match and diff_count == 1:
            total += 100 * i
            print("zone " + str(z) + " has mirror in row " + str(i))
            for r in range(len(zone)):
                print_str = zone[r]
                if r == i:
                    print_str += "<"
                print(print_str)
            print()
            continue

        #generate column map and repeat
        zone_by_cols = []
        for c in range(len(zone[0])):
            col = ""
            for r in zone:
                col += r[c]
            zone_by_cols.append(col)

        for i in range(len(zone_by_cols)):
            offset = 0
            is_match = False
            diff_count = 0
            while True:
                if (i+offset) >= len(zone_by_cols) or ((i-1) - offset) < 0:
                    break

                is_match = True
                l_1 = zone_by_cols[i+offset]
                l_2 = zone_by_cols[(i-1)-offset]

                diff_count += difference_count(l_1, l_2)

                if diff_count > 1:
                    is_match = False
                    break
                offset += 1
        
            if is_match and diff_count == 1:
                break
        



        if is_match and diff_count == 1:
            total += i
            print("zone " + str(z) + " has mirror in col " + str(i))
            for c in range(len(zone_by_cols)):
                print_str = zone_by_cols[c]
                if c == i:
                    print_str += "<"
                print(print_str)
            print()
            continue

print("total:")
print(total)
    #create the zone by col map if no match found


