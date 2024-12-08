with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input_processed.txt", "r") as file:
    count = {}
    for line in file:
        line = line.rstrip("\n")
        value = line.split("|")[0]
        if value not in count:
            count[value] = 0
        count[value] += 1

for key in count:
    print(key + ": " + str(count[key]))

print(len(count))