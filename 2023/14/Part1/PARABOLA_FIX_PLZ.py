def push_north(grid):
    for k in range(len(grid)):
        for i in range(k, 0, -1):
            line_cur = grid[i]
            line_prev = grid[i-1]

            for j in range(len(line_cur)):
                char_cur = line_cur[j]
                char_prev = line_prev[j]

                if char_cur == "O" and char_prev == ".":
                    grid[i] = line_cur[:j] + "." + line_cur[j+1:]
                    grid[i-1] = line_prev[:j] + "O" + line_prev[j+1:]
                    line_cur = grid[i]
                    line_prev = grid[i-1]

def push_south(grid):
    for k in range(len(grid)):
        for i in range(len(grid)-k-1, len(grid)-1):
            line_cur = grid[i]
            line_next = grid[i+1]

            for j in range(len(line_cur)):
                char_cur = line_cur[j]
                char_next = line_next[j]

                if char_cur == "O" and char_next == ".":
                    grid[i] = line_cur[:j] + "." + line_cur[j+1:]
                    grid[i+1] = line_next[:j] + "O" + line_next[j+1:]
                    line_cur = grid[i]
                    line_next = grid[i+1]

def push_west(grid):
    for k in range(len(grid)):
        for i in range(len(grid[k])):
            for j in range(i, 0, -1):
                #shift left if possible
                if grid[k][j] == "O" and grid[k][j-1] == ".":
                    grid[k] = grid[k][:j-1] + "O." + grid[k][j+1:]

def push_east(grid):
    for k in range(len(grid)):
        for i in range(len(grid[k])):
            for j in range(len(grid[k])-1-i,len(grid[k])-1):
                #shift right if possible
                char1 = grid[k][j]
                char2 = grid[k][j+1]
                if char1 == "O" and char2 == ".":
                    grid[k] = grid[k][:j] + ".O" + grid[k][j+2:]


with open("D:\\Code\\Advent of Code 2023\\Dec14\\Part1\\input.txt", "r") as file:
    lines = list(file)
  
    line_count = 0
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")

    for l in lines:
        print(l)

    #run 1 cycle
    cycle_list = []
    last_cycle = ""
    iterations = 0
    while True:
        iterations += 1
        if iterations % 10 == 0:
            print("iteration: " + str(iterations))
        cycle_str = ""
        for l in lines:
            cycle_str += l

        if cycle_str not in cycle_list:
            cycle_list.append(cycle_str)
        else:
            cycle_list.append(cycle_str)
            last_cycle = cycle_str
            break

        push_north(lines)
        push_west(lines)
        push_south(lines)
        push_east(lines)

    cycle_start = None
    cycle_end = None
    
    for i in range(len(cycle_list)):
        if last_cycle == cycle_list[i]:
            if cycle_start is None:
                cycle_start = i
            else:
                cycle_end = i
                break

    print("cycle start: " + str(cycle_start))
    print(cycle_list[cycle_start])
    print("cycle end: " + str(cycle_end))
    print(cycle_list[cycle_end])
    cycle_length = cycle_end - cycle_start
    print("cycle length: " + str(cycle_length))
    print()
    for i in range(len(cycle_list)):
        print(str(i) + ": " + str((i - cycle_start) % cycle_length))
    print()


    print()
    val = (1000000000-cycle_start) % cycle_length

    print("billionth cycle value: " + str(val))

    #print(cycle_list[val])
    billionth_cycle = cycle_list[val + cycle_start]
    line_length = len(lines[0])
    iterations = len(billionth_cycle) // line_length

    new_grid = []
    pos = 0

    for i in range(iterations):   
        first_pos = i*line_length
        second_pos = (i+1)*line_length
        new_grid.append(billionth_cycle[first_pos:second_pos])
    print() 

    lines = len(new_grid)
    total = 0
    multiplier = len(new_grid)
    for line in new_grid:
        matches = 0
        for char in line:
            if char == "O":
                matches += 1
                total += multiplier
        print(line + " " + str(multiplier) + "*" + str(matches))
        
        multiplier -= 1

    print()
    print(total)



    print()
    # for line in lines:
    #     multiplier -= 1
    #     line_total = 0
    #     for char in line:
    #         if char == "O":
    #             line_total += 1
    #     print(str(total) + " + (" + str(line_total) + "*" + str(multiplier) + ") = " + str(total + (line_total * multiplier)))
    #     total += line_total * multiplier
    
    print("_______________________________________")
    # print(total)

