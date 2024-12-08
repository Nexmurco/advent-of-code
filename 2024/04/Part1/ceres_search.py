from enum import Enum

class Direction(Enum):
    UP = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN = 5
    DOWN_LEFT = 6
    LEFT = 7
    UP_LEFT = 8

dir_tuple_dict = {
    Direction.UP: (0, 1),
    Direction.UP_RIGHT: (1,1),
    Direction.RIGHT: (1,0),
    Direction.DOWN_RIGHT: (1, -1),
    Direction.DOWN: (0, -1),
    Direction.DOWN_LEFT: (-1, -1),
    Direction.LEFT: (-1, 0),
    Direction.UP_LEFT: (-1, 1)
}

letter_map = {
    "X": "M",
    "M": "A",
    "A": "S"
}

sum = 0

def search_letter(pos, max_vals, currentLetter, grid, count, dir, level):
    global sum
    #check for out of bounds
    level += 1
    if pos[0] >= max_vals[0] or pos[1] >= max_vals[1] or pos[0] < 0 or pos[1] < 0:
        return
    
    #check if the position is the letter we are searching for
    if grid[pos[0]][pos[1]] == currentLetter:
        #if we are at S then return 1
        if currentLetter == "S":
            sum += 1
            return
        #if we are at X then search in every direction
        elif currentLetter == "X":
            for d in Direction:
                newpos = tuple(map(lambda i, j: i + j, pos, dir_tuple_dict[d]))
                search_letter(newpos, max_vals, letter_map[currentLetter], grid, count, d, level)
            return 
        #if we are at an in between letter, continue the search but in the same direction
        else:
            newpos = tuple(map(lambda i, j: i + j, pos, dir_tuple_dict[dir]))
            search_letter(newpos, max_vals, letter_map[currentLetter], grid, count, dir, level)
    
    return
            


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\04\\Input\\input.txt", "r") as file:
    
    sum = 0

    lines = []
    for line in file:
        line = line.rstrip("\n")
        lines.append(line)


    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            char = line[j]
            search_letter((j, i), (len(line), len(lines)), "X", lines, 0, None, 0)



    print("-----------")
    print("sum: " + str(sum))
    