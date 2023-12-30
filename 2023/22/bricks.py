with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\22\\test.txt", "r") as file:
    lines = list(file)
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        line = lines[i]
        for j in range(len(line)):