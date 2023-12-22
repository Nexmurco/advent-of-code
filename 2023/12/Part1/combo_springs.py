def character_match(char1, char2):
    if char1 == char2:
        return True
    elif char1 == "?" and (char2 == "." or char2 == "#"):
        return True
    elif char2 == "?" and (char1 == "." or char1 == "#"):
        return True
    return False

import re
total_arrangements = 0

fout = open(".\\Dec12\\Part1\\output-1.txt", "w")

with open("D:\\Code\\Advent of Code 2023\\Dec12\\Part1\\input.txt", "r") as file:
    lines = list(file)
    spring_data_list = []
    for line in lines:
        line = line.rstrip("\n")
        line_split = line.split(" ")
        data_arrangement = re.sub('\.\.+', '.', line_split[0]).strip(".")
        data_numeric = [int(num) for num in line_split[1].split(",")]

        #the minimum number of characters needed is the sum of the numbers +1 for every in between
        # so 1,6,5 -> 1 + 1 + 6 + 1 + 5 = 14

        min_chars = sum(data_numeric) + len(data_numeric) - 1
        print(data_arrangement)
        print(data_numeric)
        print(str(min_chars) + " - " + str(len(data_arrangement)) + " = " + str(len(data_arrangement) - min_chars))
        #produce the minimum required output to produce the arrangement:
        
        min_arrangement = ""
        for num in data_numeric:
            for i in range(num):
                min_arrangement += "#"
            min_arrangement += "."
        min_arrangement = min_arrangement.strip(".")

        print(min_arrangement)

        #generate the insertion position map
        insertion_map = {}
        insertion_map[0] = 0
        insertion_map_value = 0
        insertion_map_key = 0
        
        insertion_map_value = min_arrangement.find(".", insertion_map_value)
        while insertion_map_value != -1:
            insertion_map_key += 1
            insertion_map[insertion_map_key] = insertion_map_value
            insertion_map_value = min_arrangement.find(".", insertion_map_value+1)

        #add last value
        insertion_map[insertion_map_key + 1] = len(min_arrangement)
        print(insertion_map)


        #generate the combinations of possible insertions

        combinations = []
        choices = len(data_arrangement) - len(min_arrangement)
        values = len(data_numeric) + 1

        #generate all combinations and fill the combo_list with them
        combo_list = []

        position_list = []
        for i in range(choices):
            position_list.append(0)
        
        combo_list.append(position_list.copy())

        end_pos = len(position_list) - 1
        cur_pos = end_pos

        while choices > 0 and position_list[0] < values:
            #add to last value, if that value reaches max value, add one to preceding number
            #go backwards as far as possible, then from that position go forward setting all right hand values equal to farthes left value changed
            
            #increment current position
            position_list[cur_pos] += 1

            if position_list[cur_pos] >= values:
                #backtrack 1 position
                cur_pos = cur_pos - 1
            elif cur_pos != end_pos:
                #forward propogate number
                for i in range(cur_pos, end_pos+1):
                    position_list[i] = position_list[cur_pos]
                cur_pos = end_pos
                #append to list
                combo_list.append(position_list.copy())
            else:
                #append to list
                combo_list.append(position_list.copy())

        #now insert
        arrangement_list = []
        for combo in combo_list:
            new_arrangement = min_arrangement
            for insert_key in list(reversed(combo)):
                insert_pos = insertion_map[insert_key]
                new_arrangement = new_arrangement[:insert_pos] + "." + new_arrangement[insert_pos:]
            arrangement_list.append(new_arrangement)

        valid_arrangements = 0

        for a in arrangement_list:
            #check if the arrangement is valid for the wildcards
            arrangement_match = True
            for i in range(len(a)):
                if not character_match(a[i], data_arrangement[i]):
                    arrangement_match = False
                    break
            if arrangement_match:
                valid_arrangements += 1

        print(valid_arrangements)
        print(valid_arrangements, file=fout)
        total_arrangements += valid_arrangements
print()
print(total_arrangements)
fout.close()

        
        

        
                






    #in the arrangement data, ? represents and unknown spring, # represents a damaged spring

    #our numeric data says the length of each run of broken springs, the count of them is how many runs there are

