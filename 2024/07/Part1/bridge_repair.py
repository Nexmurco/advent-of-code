

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\07\\Input\\input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.rstrip("\n")
        split = line.split(": ")
        answer = int(split[0])
        inputs = split[1].split(" ")
        first_input = int(inputs.pop(0))
        #print("--------")
        #print(inputs)
        for i in range(2**len(inputs)):
            operators = bin(i)[2:].zfill(len(inputs))
            total = first_input
            eq_string = str(answer) + " = "
            eq_string += str(first_input)
            for j in range(len(inputs)):
                
                if operators[j] == "1":
                    eq_string += "+"
                    total += int(inputs[j])
                else:
                    eq_string += "*"
                    total *= int(inputs[j])
                eq_string += inputs[j]
                if total > answer:
                    break

            #print(eq_string + " = " + str(total))
            if total == answer:
                sum += answer
                break
                #combine all the inputs using the operator list
                
    print(sum)