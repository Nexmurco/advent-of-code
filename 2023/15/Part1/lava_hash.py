with open("D:\\Code\\Advent of Code 2023\\Dec15\\Part1\\input.txt", "r") as file:
    lines = list(file)
    instruction_line = lines[0]
    instruction_line = instruction_line.rstrip("\n")
    instructions = instruction_line.split(",")

    total = 0
    for i in instructions:
        cur = 0
        for char in i:
            cur += ord(char)
            cur *= 17
            cur %= 256
        total += cur

    print(total)

