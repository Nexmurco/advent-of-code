max_x = -1
max_y = -1

def out_of_bounds(pos):
    global max_x, max_y
    return pos[0] < 0 or pos[0] > max_x or pos[1] < 0 or pos[1] > max_y


def increment_positions(pos1, pos2):
    increment = (pos1[0] - pos2[0], pos1[1] - pos2[1])
    return(pos2[0] - increment[0], pos2[1] - increment[1])

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\08\\Input\\input.txt", "r") as file:
    sum = 0
    lines = []
    
    for line in file:
        lines.append(line.rstrip("\n"))

    symbols = {}
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            char = line[x]
            if char != ".":
                if char not in symbols:
                    symbols[char] = []
                symbols[char].append((x,y))

    antinodes = set(())

    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    #print(max_x)
    #print(max_y)

    for character in symbols:
        positions = symbols[character]
        for i in range(len(positions)):
            ##print(i)
            for j in range(i+1, len(positions)):
                ##print()
                a1 = increment_positions(positions[i], positions[j])
                a2 = increment_positions(positions[j], positions[i])
                ##print(str(positions[i]) + " " + str(positions[j]))
                ##print(a1)
                ##print(a1)
                ##print()
                if not out_of_bounds(a1):
                    antinodes.add(a1)
                if not out_of_bounds(a2):
                    antinodes.add(a2)


    
    print(symbols.keys)
    print(antinodes)
    print(len(antinodes))