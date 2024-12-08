#stolen from stack exchange https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
import copy

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\07\\Input\\input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.rstrip("\n")
        split = line.split(": ")
        answer = int(split[0])
        values = split[1].split(" ")
        first_input = values.pop(0)

        for i in range(3**len(values)):
            inputs = copy.deepcopy(values)
            operators = ternary(i).zfill(len(inputs))
            
            total = first_input
            count = 0

            while inputs:
                next_val = inputs.pop(0)
                if operators[count] == "1":
                    total = str(int(total) + int(next_val))
                elif operators[count] == "2":
                    total = str(int(total) * int(next_val))
                else:
                    total += next_val
                    
                if int(total) > answer:
                    break
                count += 1

            if int(total) == answer:
                sum += answer
                break
                #combine all the inputs using the operator list
                
    print(sum)