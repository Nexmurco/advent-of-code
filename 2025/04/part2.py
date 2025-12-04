import sys
input_file = sys.argv[1]

bool_grid = []
adj_grid = []
adj_positions = [-1,0,1]


#take puzzle input and make a 2d list showing positions
with open(input_file, "r") as inputs:
    for input in inputs:
        line = input.rstrip()
        row = []
        for char in line:
            if char == "@":
                row.append(True)
            else:
                row.append(False)
        bool_grid.append(row)


count_rows = len(bool_grid)
count_cols = len(bool_grid[0])

sum = 0
continue_removal = True
iteration = 0
clearance = 4

while(continue_removal):
    iteration += 1
    print("iteration " + str(iteration))
    #create a new adj grid
    adj_grid = []
    for i in range(count_rows):
        adj_grid.append([0] * count_cols)

    #populate the adj grid
    for i in range(count_rows):
        for j in range(count_cols):
            if bool_grid[i][j]:
                #go in each direction and add 1
                for x in adj_positions:
                    #do not go out of bounds
                    if i == 0 and x == -1:
                        continue
                    if i == count_rows-1 and x == 1:
                        continue

                    for y in adj_positions:
                        #do not add to the current space
                        if y == 0 and x == 0:
                            continue
                        #do not go out of bounds
                        if j == 0 and y == -1:
                            continue
                        if j == count_cols-1 and y == 1:
                            continue
                        adj_grid[i+x][j+y] += 1

    #add the locations that have clearance to the sum
    #remove them from the bool_grid
    iteration_sum = 0
    for i in range(count_rows):
        for j in range(count_cols):
            if bool_grid[i][j] == True and adj_grid[i][j] < clearance:
                iteration_sum += 1
                bool_grid[i][j] = False
    print("removed " + str(iteration_sum) + " positions")
    print()
    sum += iteration_sum
    if iteration_sum == 0:
        continue_removal = False
    #sanity check, no infinite loops please
    if iteration == 10000:
        continue_removal = False

print("GRAND TOTAL")
print(sum)
