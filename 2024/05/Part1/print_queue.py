
with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input.txt", "r") as file:
    
    sum = 0

    lines = []

    ordering = {}
    reverse_ordering = {}
    number_sizes = {}
    reverse_number_sizes = {}
    data = []
    collect_ordering = True

    for line in file:
        line = line.rstrip("\n")
        if collect_ordering:
            if line == "":
                collect_ordering = False
            else:
                values = line.split("|")
                if values[0] not in ordering:
                    ordering[values[0]] = []
                ordering[values[0]].append(values[1])

                if values[1] not in reverse_ordering:
                    reverse_ordering[values[1]] = []
                reverse_ordering[values[1]].append(values[0])
        
        else:
            data.append(line.split(","))
    
    valid_data_set = []
    for d in data:
        valid_data = True
        print("-------")
        print(d)
        for i in range(len(d)):
            for j in range(i+1, len(d)):
                if d[i] not in ordering or d[j] not in ordering[d[i]]:
                    valid_data = False
                    break
        if valid_data:
            valid_data_set.append(d)

    for d in valid_data_set:
        sum += int(d[int(len(d)/2)])

    print(sum)
        



                