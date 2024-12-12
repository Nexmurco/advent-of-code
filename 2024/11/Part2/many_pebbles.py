def make_rocks(rock, level):
    global max_level
    global count

    if(count % 100000 == 0):
        print(count)

    if level == max_level:
        return 1

    total_rocks = 0
    if rock in rock_map and rock_map_jumps[rock] + level <= max_level:
            for r in rock_map[rock]:
                count += r[1]
                total_rocks += make_rocks(r[0], level + r[1])
    
    else:
        if rock == "0":
            total_rocks += make_rocks("1", level + 1)
        elif len(rock) % 2 == 0:
                    rock_l = rock[:int((len(rock)/2))].lstrip("0")
                    rock_r = rock[int(((len(rock)/2))):].lstrip("0")
                    if rock_l == "":
                        rock_l = "0"
                    if rock_r == "":
                        rock_r = "0"
                    total_rocks += make_rocks(rock_l, level + 1)
                    total_rocks += make_rocks(rock_r, level + 1)
        else:
            total_rocks += make_rocks(str(int(rock) * 2024), level + 1)
    
    return total_rocks
        


rock_map_jumps = {
    "0": 4,
    "1": 3,
    "2": 3,
    "3": 3,
    "4": 3,
    "5": 5,
    "6": 5,
    "7": 5,
    "8": 5,
    "9": 5
}

rock_map = {
    "0": [("2", 4), ("0", 4), ("2", 4), ("4", 4)],
    "1": [("2", 3), ("0", 3), ("2", 3), ("4", 3)],
    "2": [("4", 3), ("0", 3), ("4", 3), ("8", 3)],
    "3": [("6", 3), ("0", 3), ("7", 3), ("2", 3)],
    "4": [("8", 3), ("0", 3), ("9", 3), ("6", 3)],
    "5": [("2", 5), ("0", 5), ("2", 5), ("4", 5), ("2", 5), ("8", 5), ("8", 5), ("0", 5)],
    "6": [("2", 5), ("4", 5), ("5", 5), ("7", 5), ("9", 5), ("4", 5), ("5", 5), ("6", 5)],
    "7": [("2", 5), ("8", 5), ("6", 5), ("7", 5), ("6", 5), ("0", 5), ("3", 5), ("2", 5)],
    "8": [("3", 5), ("2", 5), ("7", 5), ("7", 5), ("2", 5), ("6", 5), ("8", 4)],
    "9": [("3", 5), ("6", 5), ("8", 5), ("6", 5), ("9", 5), ("1", 5), ("8", 5), ("4", 5)],
}


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\11\\Input\\input_test.txt", "r") as file:
    for line in file:
        input = line.rstrip("\n")
    
    rocks = input.split(" ")
    print(rocks)

    max_level = 75
    count = 0
    total = 0

    for rock in rocks:
        total += make_rocks(rock, 0)

    print(total)

    
    