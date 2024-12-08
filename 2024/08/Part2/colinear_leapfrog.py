max_x = -1
max_y = -1

def out_of_bounds(pos):
    global max_x, max_y
    return pos[0] < 0 or pos[0] > max_x or pos[1] < 0 or pos[1] > max_y


def increment_positions(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])

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

    for character in symbols:
        positions = symbols[character]
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                pos1 = positions[i]
                pos2 = positions[j]
                jump1 = increment_positions(pos1, pos2)
                jump2 = increment_positions(pos2, pos1)
                
                loop = True
                pos = pos2
                while loop:
                    antinodes.add(pos)
                    pos = (pos[0] + jump1[0], pos[1] + jump1[1])
                    if out_of_bounds(pos):
                        loop = False
                
                loop = True
                pos = pos1
                while loop:
                    antinodes.add(pos)
                    pos = (pos[0] + jump2[0], pos[1] + jump2[1])
                    if out_of_bounds(pos):
                        loop = False



    
    print(symbols.keys())
    print(antinodes)
    print(len(antinodes))


    # for a in antinodes:
    #     s = lines[a[1]]
    #     s = s[:a[0]] + "#" + s[a[0] + 1:]
    #     lines[a[1]] = s

    # for line in lines:
    #     print(line)