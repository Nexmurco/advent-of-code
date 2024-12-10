with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\09\\Input\\input_test.txt", "r") as file:
    line = ""
    
    for f in file:
        line = f.rstrip("\n")

    space_array = []
    #get an ordered list of where empty spaces start
    empty_start_spaces = []
    #make a mapping of how long each empty space continues
    empty_space_sizes = {}

    file_start_spaces = {}
    file_sizes = {}

    is_free_space = True
    id = 0
    for char in line:
        is_free_space = not is_free_space

        if is_free_space:
            if int(char) > 0:
                start_pos = len(space_array)
                empty_start_spaces.append(start_pos)
                empty_space_sizes[start_pos] = int(char)

            for i in range(int(char)):
                space_array.append(".")
        else:
            file_start_spaces[id] = len(space_array)
            file_sizes[id] = int(char)
            for i in range(int(char)):
                space_array.append(id)
            id += 1
    
    while id > 0:
        id -= 1
        cur_file_size = file_sizes[id]
        #get first empty space that can fit the file
        start_pos = -1
        start_pos_index = -1
        for p in range(len(empty_start_spaces)):
            pos = empty_start_spaces[p]
            if empty_space_sizes[pos] >= cur_file_size:
                start_pos = pos
                start_pos_index = p
                break

        #move file into new location if one was found
        if start_pos != -1:
            for i in range(cur_file_size):
                space_array[start_pos + i] = id
                space_array[file_start_spaces[id] + i] = "."

            #update file size data
            
            #move the start index forward the number of replaced spaces
            empty_start_spaces[p] += file_sizes[id]
            #remove the old empty space dict entry
            size = empty_space_sizes.pop(start_pos) - file_sizes[id]
            #if there are any free spaces remaining, update and re-add the empty space size
            if size >= 0:
                empty_space_sizes[empty_start_spaces[p]] = size
            #if not, remove the start index from the start spaces so it is no longer used
            else:
                empty_start_spaces.pop(p)


    #get checksum
    sum = 0
    for i in range(len(space_array)):
        if space_array[i] != ".":
            sum += i * space_array[i]

    print(sum)