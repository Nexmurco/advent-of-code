from enum import Enum

def tuple_add(a, b):
    val = (a[0] + b[0], a[1] + b[1])
    return val

def is_in_bounds(pos):
    global max_x
    global max_y
    return pos[0] < max_x and pos[0] >= 0 and pos[1] < max_y and pos[1] >= 0

class Dir(Enum):
    North = 1
    East = 2
    South = 3
    West = 4


arrow_movement = {
    "^": (0,-1),
    ">": (1,0),
    "v": (0,1),
    "<": (-1,0)
}

movement = {
    Dir.North: (0,-1),
    Dir.East: (1,0),
    Dir.South: (0,1),
    Dir.West: (-1,0)
}

keypad_numeric = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [None, 0, "A"]]
keypad_directional = [[None, "^", "A"], ["<", "v", ">"]]

numeric_dict = {("7", "8"): ">", ("7", "9"): ">>", ("7", "4"): "v", ("7", "5"): ">v", ("7", "6"): ">>v", ("7", "1"): "vv", ("7", "2"): ">vv", ("7", "3"): ">>vv", ("7", "0"): ">vvv", ("7", "A"): ">>vvv", ("8", "7"): "<", ("8", "9"): ">", ("8", "4"): "v<", ("8", "5"): "v", ("8", "6"): ">v", ("8", "1"): "vv<", ("8", "2"): "vv", ("8", "3"): ">vv", ("8", "0"): "vvv", ("8", "A"): ">vvv", ("9", "7"): "<<", ("9", "8"): "<", ("9", "4"): "v<<", ("9", "5"): "v<", ("9", "6"): "v", ("9", "1"): "vv<<", ("9", "2"): "vv<", ("9", "3"): "vv", ("9", "0"): "vvv<", ("9", "A"): "vvv", ("4", "7"): "^", ("4", "8"): "^>", ("4", "9"): "^>>", ("4", "5"): ">", ("4", "6"): ">>", ("4", "1"): "v", ("4", "2"): ">v", ("4", "3"): ">>v", ("4", "0"): ">vv", ("4", "A"): ">>vv", ("5", "7"): "^<", ("5", "8"): "^", ("5", "9"): "^>", ("5", "4"): "<", ("5", "6"): ">", ("5", "1"): "v<", ("5", "2"): "v", ("5", "3"): ">v", ("5", "0"): "vv", ("5", "A"): ">vv", ("6", "7"): "^<<", ("6", "8"): "^<", ("6", "9"): "^", ("6", "4"): "<<", ("6", "5"): "<", ("6", "1"): "v<<", ("6", "2"): "v<", ("6", "3"): "v", ("6", "0"): "vv<", ("6", "A"): "vv", ("1", "7"): "^^", ("1", "8"): "^^>", ("1", "9"): "^^>>", ("1", "4"): "^", ("1", "5"): "^>", ("1", "6"): "^>>", ("1", "2"): ">", ("1", "3"): ">>", ("1", "0"): ">v", ("1", "A"): ">>v", ("2", "7"): "^^<", ("2", "8"): "^^", ("2", "9"): "^^>", ("2", "4"): "^<", ("2", "5"): "^", ("2", "6"): "^>", ("2", "1"): "<", ("2", "3"): ">", ("2", "0"): "v", ("2", "A"): ">v", ("3", "7"): "^^<<", ("3", "8"): "^^<", ("3", "9"): "^^", ("3", "4"): "^<<", ("3", "5"): "^<", ("3", "6"): "^", ("3", "1"): "<<", ("3", "2"): "<", ("3", "0"): "v<", ("3", "A"): "v", ("0", "7"): "^^^<", ("0", "8"): "^^^", ("0", "9"): "^^^>", ("0", "4"): "^^<", ("0", "5"): "^^", ("0", "6"): "^^>", ("0", "1"): "^<", ("0", "2"): "^", ("0", "3"): "^>", ("0", "A"): ">", ("A", "7"): "^^^<<", ("A", "8"): "^^^<", ("A", "9"): "^^^", ("A", "4"): "^^<<", ("A", "5"): "^^<", ("A", "6"): "^^", ("A", "1"): "^<<", ("A", "2"): "^<", ("A", "3"): "^", ("A", "0"): "<"}
direction_dict = {("^", "A"): ">", ("^", "<"): "v<", ("^", "v"): "v", ("^", ">"): ">v", ("A", "^"): "<", ("A", "<"): "v<<", ("A", "v"): "v<", ("A", ">"): "v", ("<", "^"): ">^", ("<", "A"): ">>^", ("<", "v"): ">", ("<", ">"): ">>", ("v", "^"): "^", ("v", "A"): ">^", ("v", "<"): "<", ("v", ">"): ">", (">", "^"): "<^", (">", "A"): "^", (">", "<"): "<<", (">", "v"): "<"}

#print(keypad_numeric)
#print(keypad_directional)


for i in range(len(keypad_numeric)):
    print(keypad_numeric[i])
print()

for i in range(len(keypad_directional)):
    print(keypad_directional[i])        

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\21\\Input\\input_test.txt", "r") as file:
    codes = []
    numeric_values = []
    sum = 0
    for line in file:
        code = line.rstrip("\n")
        print(code)

        instructions1 = ""

        prev_char = "A"
        
        for i in range(len(code)):
            curr_char = code[i]
            instruction = ""
            if (prev_char, curr_char) in numeric_dict:
                instruction = numeric_dict[(prev_char, curr_char)]
            instruction += "A"
            instructions1 += instruction
            print(prev_char + ", " + curr_char + ": " + instruction)
            prev_char = curr_char
        
        print(instructions1)
        print()

        prev_char = "A"
        instructions2 = ""

        for i in range(len(instructions1)):
            curr_char = instructions1[i]
            instruction = ""
            if (prev_char, curr_char) in direction_dict:
                instruction = direction_dict[(prev_char, curr_char)]
            instruction += "A"
            instructions2 += instruction
            print(prev_char + ", " + curr_char + ": " + instruction)
            prev_char = curr_char
        
        print(instructions2)
        print()

        prev_char = "A"
        instructions3 = ""

        for i in range(len(instructions2)):
            curr_char = instructions2[i]
            instruction = ""
            if (prev_char, curr_char) in direction_dict:
                instruction = direction_dict[(prev_char, curr_char)]
            instruction += "A"
            instructions3 += instruction
            #print(str((prev_char, curr_char)) + ": " + instructions3)
            print(prev_char + ", " + curr_char + ": " + instruction)
            prev_char = curr_char
        
        print(instructions3)

        print(len(instructions3))
        print(int(code[:3]))
        print(len(instructions3) * int(code[:3]))
        sum += len(instructions3) * int(code[:3])
        print()
    
    print(sum)