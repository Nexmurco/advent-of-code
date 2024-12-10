with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\09\\Input\\input.txt", "r") as file:
    line = ""
    
    for f in file:
        line = f.rstrip("\n")

    space_array = []

    free_space = True

    id = 0
    for char in line:
        free_space = not free_space

        if free_space:
            for i in range(int(char)):
                space_array.append(".")
        else:
            for i in range(int(char)):
                space_array.append(id)
            id += 1
    
    sorting = True

    print("array size: " + str(len(space_array)))

    count = 0

    last_id = len(space_array) - 1
    first_space = 0
    while sorting:

        count += 1
        if count%1000 == 0:
            print("loop number: " + str(count))
        #print(space_array)
        #check if array is sorted
        hit_free_space = False
        sorting = False


        for item in space_array:
            if hit_free_space and item != ".":
                sorting = True
                #print("sort next element")
                break
            elif item == ".":
                hit_free_space = True
                #print("hit free space")
        
        #take last element and move it to first available space


        if sorting:
            swapped = False
            for i in range(last_id, -1, -1):
                #print("finding last id")
                temp_id = None
                if space_array[i] != ".":
                    #print("id " + str(space_array[i]) + " found at position " + str(i))
                    temp_id = space_array[i]
                    space_array[i] = "."
                    last_id = i - 1
                
                #find first open space
                if temp_id:
                    for j in range(first_space, len(space_array)):
                        #print("finding first free space")
                        if space_array[j] == ".":
                            space_array[j] = temp_id
                            swapped = True
                            first_space = j + 1
                            #print("free space found at position " + str(j))
                            break

                if swapped:
                    break

    print("sorting complete")
    print(space_array)

    #get checksum
    sum = 0
    for i in range(len(space_array)):
        if space_array[i] != ".":
            sum += i * space_array[i]

    print(sum)