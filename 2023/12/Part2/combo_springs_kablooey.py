import copy

def character_match(char1, char2):
    if char1 == char2:
        return True
    elif char1 == "?" and (char2 == "." or char2 == "#"):
        return True
    elif char2 == "?" and (char1 == "." or char1 == "#"):
        return True
    return False

def a_numerics_sum(a_list):
    sum = 0
    for a in a_list:
        sum += a["length"]
    return sum

import re
total_arrangements = 0

fout = open(".\\Dec12\\Part2\\output.txt", "w")

with open("D:\\Code\\Advent of Code 2023\\Dec12\\Part2-B\\input.txt", "r") as file:
    lines = list(file)
    spring_data_list = []
    line_count = 0

    for line in lines:
        line_count += 1
        line = line.rstrip("\n")
        line_split = line.split(" ")
        data_arrangement = line_split[0]
        data_numeric = line_split[1].split(",")

        #transform the data_arrangement and data_numeric based on problem
        data_arrangement_orig = data_arrangement + "?"
        data_arrangement = ""
        for i in range(5):
            data_arrangement += data_arrangement_orig
        
        data_arrangement = re.sub('\.\.+', '.', data_arrangement).strip(".")

        data_numeric_orig = data_numeric.copy()
        for i in range(4):
            data_numeric += data_numeric_orig.copy()

        data_numeric = [int(num) for num in data_numeric]

        #using data_numeric and data_arrangement, calculate possible arrangements

        #generate the numeric clusters from the arrangement
        data_arrangement_numeric = []

        cluster_start = None
        in_cluster = False

        require_str = ""
        for pos in range(len(data_arrangement)):
            char = data_arrangement[pos]
            
            if char in ["#","?"]:
                require_str += char


            if not in_cluster and char in ["#","?"]:
                cluster_start = pos
                in_cluster = True

            elif in_cluster and char == ".":
                length = pos - cluster_start

                data_arrangement_numeric.append({"length":length, "required_pos":require_str + "."})
                require_str = ""
                in_cluster = False

        if in_cluster:
            length = len(data_arrangement) - cluster_start
            data_arrangement_numeric.append({"length":length, "required_pos":require_str + "."})

        #now exhaustively try to fill each min arrangement value into any arrangement value left to right
        data_arrangement_lengths = []
        for d in data_arrangement_numeric:
            data_arrangement_lengths.append(d["length"])
            print(d)
        print(data_arrangement_lengths)
        print(data_numeric)
        print("---------")

        print("iterating on problem " + str(line_count) + "/" + str(len(lines)))

        first_numeric = data_numeric[0]
        
        numerics = data_numeric.copy()
        a_numerics = copy.deepcopy(data_arrangement_numeric)

        n_cur = numerics[0]

        n_stack = []
        a_stack = []

        match_count = 0
        depth = 0
        
        terminate = False
        max_depth = False
        skipped_requirement = False

        iterations = 0

        while not terminate:
            iterations += 1
            if iterations % 1000000 == 0:
                print(str(iterations) + " iterations")
            #check if our current numeric fits into any of the numerics in our sub data arrangment
            has_fit = False

            if not terminate and len(numerics) == 0:
                for a in a_numerics:
                    if "#" in a["required_pos"]:
                        skipped_requirement = True
                if not skipped_requirement:
                    match_count += 1
                max_depth = True
            else:
                n_cur = numerics[0]
            
            for i in range(len(a_numerics)):
                if (sum(numerics) + len(numerics)) > (a_numerics_sum(a_numerics) + len(a_numerics)):
                    break
                if skipped_requirement:
                    break
                if max_depth:
                    break

                a = a_numerics[0]["length"]
                if n_cur <= a:
                    has_fit = True

                    #we have a fit!
                    
                    #if numerics is on its last value, then increase the count of our matches, and go up a level
                    #pop our current number lists into the stacks
                    n_stack.append(numerics.copy())
                    a_stack.append(copy.deepcopy(a_numerics))
                    #reduce numerics by removing the values consumed
                    numerics.pop(0)
                    depth += 1

                    #remove all a-numerics values before the active one
                    #in a-numerics reduce the front value by the size of n_cur, if it reaches 0, pop it
                    a_numerics[0]["length"] -= (n_cur+1)

                    if a_numerics[0]["required_pos"][n_cur] == "#":
                        #cause failure condition, we skipped a required spot
                        skipped_requirement = True
                        break
                    a_numerics[0]["required_pos"] = a_numerics[0]["required_pos"][n_cur+1:]

                    if a_numerics[0]["length"] <= 0:
                        a_numerics.pop(0)
                    #set our current n val to be the front of the numerics list
                    break
                else:
                    if "#" in a_numerics[0]["required_pos"]:
                        skipped_requirement = True
                    a_numerics.pop(0)
                
            if not has_fit:
                #if the stack is empty, we are at top level and can terminate
                if len(n_stack) <= 0:
                    terminate = True
                    break
                
                max_depth = False
                skipped_requirement = False

                #otherwise go up a level, remove the parts we have already tried, then continue
                numerics = n_stack.pop()
                a_numerics = a_stack.pop()

                n_cur = numerics[0]
                #reduce the size of the first number we check by 1, if this makes it too small to fit n_cur into, then remove it
                
                #if this shortening operation causes us to pass a required char then fail 
                a_numerics[0]["length"] -= 1

                if a_numerics[0]["required_pos"][0] == "#":
                    #cause a failure
                    skipped_requirement = True

                a_numerics[0]["required_pos"] = a_numerics[0]["required_pos"][1:]
                if a_numerics[0]["length"] < n_cur:
                    if "#" in a_numerics[0]["required_pos"]:
                        skipped_requirement = True
                    a_numerics.pop(0)
                depth -= 1


        print(match_count)
        print(match_count, file=fout)
        total_arrangements += match_count
        print(total_arrangements)
        print("_________________")

print(total_arrangements)
fout.close()
