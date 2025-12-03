import sys
input_file = sys.argv[1]

sum = 0
digits = 12

with open(input_file, "r") as input:
    for line in input:
        line = line.rstrip()
        list_digit = []
        list_pos = []

        prev_pos = -1

        for i in range(digits):

            list_digit.append(-1)
            list_pos.append(-1)
            for j in range(prev_pos + 1, len(line) - (digits - (i + 1))):
                char = line[j]
                if int(char) > int(list_digit[i]):
                    list_digit[i] = char
                    list_pos[i] = j
            prev_pos = list_pos[i]

        value = ""
        for digit in list_digit:
            value += digit

        sum += int(value)
    
print("sum: " + str(sum))
