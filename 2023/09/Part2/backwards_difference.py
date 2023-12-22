with open("D:\\Code\\Advent of Code 2023\\Dec09\\Part2\\input.txt", "r") as file:
    lines = list(file)
    sum = 0
    for line in lines:
        line = line.rstrip("\n")
        numbers = line.split(" ")
        numbers = [int(num) for num in numbers]
        numbers = list(reversed(numbers))

        is_zero_vector = False
        difference_matrix = []
        difference_line = numbers
        difference_matrix.append(numbers)
        
        while not is_zero_vector:
            difference_line_prev = difference_line
            difference_line = []
            for i in range(len(difference_line_prev)-1):
                difference_line.append(int(difference_line_prev[i+1])-int(difference_line_prev[i]))
            difference_matrix.append(difference_line)

            #check for all zeros
            is_zero_vector = True
            for j in difference_line:
                if j != 0:
                    is_zero_vector = False


            

        for d in range(len(difference_matrix)-1, 0, -1):
            #add the last element of the current list to the last element of the previous list
            last_element = difference_matrix[d][len(difference_matrix[d])-1]
            last_element_higher = difference_matrix[d-1][len(difference_matrix[d-1])-1]
            new_element = last_element + last_element_higher
            difference_matrix[d-1].append(new_element)
        

            
        sum += difference_matrix[0][len(difference_matrix[0])-1]

print(sum)

