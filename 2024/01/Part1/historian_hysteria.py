with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\01\\Part1\\input.txt", "r") as file:
    sum = 0
    col1 = []
    col2 = []
    for line in file:
        line = line.rstrip("\n")
        values = line.split()
        col1.append(int(values[0]))
        col2.append(int(values[1]))

    col1.sort()
    col2.sort()

    for index in range(0, len(col1)):
        difference = abs(col1[index] - col2[index])
        sum += difference

    print("-----------")
    print("sum: " + str(sum))
    