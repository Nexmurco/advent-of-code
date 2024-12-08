import copy


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\05\\Input\\input_test.txt", "r") as file:
    
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

    #sort the values into a list
    order = copy.deepcopy(ordering)
    print(list(order.keys()))
    key = list(order.keys())[0]

    print("ordering")
    print(ordering)
    print("reverse_ordering")
    print(reverse_ordering)

    sorted_values = []
    value_indeces = {}



    

    while order:
        break
        

        
        if key not in order:
            key = list(order.keys())[0]

        prev_key = key  
        key = order[key].pop(0)
        print()
        print("-------------")
        print("new key: " + str(key))
        print("sorted values: " + str(sorted_values))
        print("-------------")
        print()
        if len(order[prev_key]) == 0:
            order.pop(prev_key, None)

    for val in list(ordering.keys()):
        if val not in sorted_values:
            sorted_values.insert(0, val)
            break


    print(sorted_values)

    sort_order = {}
    for index in range(len(sorted_values)):
        sort_order[sorted_values[index]] = index
    
    print(sort_order)
    
    valid_data_set = []
    invalid_data_set = []
    for d in data:
        valid_data = True
        #print("-------")
        #print(d)
        for i in range(len(d)):
            for j in range(i+1, len(d)):
                if d[i] not in ordering or d[j] not in ordering[d[i]]:
                    valid_data = False
                    break
        if valid_data:
            #print("Appending")
            valid_data_set.append(d)
        else:
            invalid_data_set.append(d)


    #now fix the ordering of the incorrect data lists
    for d in valid_data_set:
        #print("---------")
        #print(d)
        d.sort(key=lambda val: sort_order[val])
        #print(d)

    for d in invalid_data_set:
        d_temp = copy.copy(d)
        d_temp.sort(key=lambda val: sort_order[val])

              

    



    for d in invalid_data_set:
        sum += int(d[int(len(d)/2)])

    print(sum)
        



                