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

print(keypad_numeric)
print(keypad_directional)

print(int("029"))

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\21\\Input\\input_test.txt", "r") as file:
    codes = []
    numeric_values = []
    for line in file:
        line = line.rstrip("\n")