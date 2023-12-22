#get the range of values the numbers are stored in and calculate all the surrounding values
sum = 0

symbols = "-$%+&/@#="
gear_symbol ="*"

with open("D:\\Code\\Advent of Code 2023\\Dec 3\\Part 1\\input.txt", "r") as file:
    line_prev = None
    line_cur = None
    line_next = None
    counter = -1

    gears = {}

    for line in file:
        counter += 1
        #print()
        #print(str(counter) + ": ")
        line = line.rstrip("\n")
        line_prev = line_cur
        line_cur = line_next
        line_next = line

        if line_cur != None:
            #combine numbers into group
            group_start = None
            group_end = None

            group_list = []

            for i in range(len(line_cur)):
                if line_cur[i].isdigit():
                    if group_start is None:
                        group_start = i
                    group_end = i
                else:
                    if group_start is not None:
                        group_list.append((group_start, group_end))
                    group_start = None
                    group_end = None

            if group_start is not None:
                group_list.append((group_start, group_end))
            
            #we now have all the groupings, go around each group and check if there are any symbols

            touches_symbol = False

            for group in group_list:
                touches_symbol = False
                #check if prev term in bounds
                character_list = []

                left_val = group[0]-1
                if group[0]-1 >= 0:
                    character_list.append({"char": line_cur[left_val],"pos": (left_val,counter)})
                    if line_next is not None:
                        character_list.append({"char": line_next[left_val],"pos": (left_val,counter+1)})
                    if line_prev is not None:
                        character_list.append({"char": line_prev[left_val],"pos": (left_val,counter-1)})
                
                right_val = group[1]+1
                if right_val <= len(line_cur)-1:
                    character_list.append({"char": line_cur[right_val], "pos": (right_val,counter)})
                    if line_next is not None:
                        character_list.append({"char": line_next[right_val],"pos": (right_val,counter+1)})
                    if line_prev is not None:
                        character_list.append({"char": line_prev[right_val],"pos": (right_val,counter-1)})

                for i in range(group[0], group[1]+1):
                    if line_next is not None:
                        character_list.append({"char": line_next[i],"pos": (i,counter+1)})
                    if line_prev is not None:
                        character_list.append({"char": line_prev[i],"pos": (i,counter-1)})
                    #check above and below
                
                number = int(line_cur[group[0]:group[1]+1])

                megaChar = ""
                for info in character_list:
                    char = info["char"]
                    megaChar += char
                    if symbols.find(char) != -1:
                        touches_symbol = True
                    position = info["pos"]
                    
                    if char == gear_symbol:
                        if position not in gears.keys():
                            gears[position] = []
                        gears[position].append(number)
                            
                        #check if gears already has that position gear:
                if touches_symbol:
                    pass
                    #sum+= number
                    #print(line_cur[group[0]:group[1]+1])
    gearCount = 0
    for p in gears:
        if len(gears[p]) == 2:
            gearCount += 1
            print("gear at: " + str(p))
            print(str(gears[p][0]) + " * " + str(gears[p][1]))
            sum += gears[p][0] * gears[p][1]


print("gears: " + str(gearCount))
print(sum)