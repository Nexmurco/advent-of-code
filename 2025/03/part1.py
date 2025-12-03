import sys
input_file = sys.argv[1]

sum = 0

with open(input_file, "r") as input:
    for line in input:

        first_char = -1
        first_pos = -1
        second_char = -1
        second_pos = -1

        line = line.rstrip()
        

        for i in range(len(line) - 1):
            char = line[i]
            if int(char) > int(first_char):
                first_char = char
                first_pos = i

        for j in range(first_pos+1, len(line)):
            char = line[j]
            if int(char) > int(second_char):
                second_char = char
                second_pos = j

        sum += int(first_char + second_char)
    
print("sum: " + str(sum))
