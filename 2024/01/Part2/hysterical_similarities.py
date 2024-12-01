with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\01\\Input\\input.txt", "r") as file:
    sum = 0
    col1 = []
    col2 = []
    for line in file:
        line = line.rstrip("\n")
        values = line.split()
        col1.append(int(values[0]))
        col2.append(int(values[1]))


    count_map = {}

    for index in range(0, len(col2)):
        value = col2[index]
        if(value not in count_map):
            count_map[value] = 0

        count_map[value] += 1

    for index in range(0, len(col1)):
        value = col1[index]
        if value in count_map:
            sum += value * count_map[value]


    print("-----------")
    print("sum: " + str(sum))
    