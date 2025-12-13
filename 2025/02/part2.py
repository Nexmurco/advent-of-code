import sys
input_file = sys.argv[1]

intervals = []
with open(input_file, "r") as input:
    for line in input:
        ranges = line.split(",")
        for r in ranges:
            pair = r.split("-")
            intervals.append((pair[0], pair[1]))

divisibility_dict = {}
#check the digit count each interval could be divisible by and add it to that subprocess


invalid_ids = []

for pair in pairs_trimmed:
    print(pair)
    lower = pair[0]
    upper = pair[1]

    length = len(lower)

    lower_front = int(lower[:length//2])
    upper_front = int(upper[:length//2])
    lower_back = int(lower[length//2:])
    upper_back = int(upper[length//2:])


    #there is one value per distance between lower front and upper front
    for number in range(lower_front, upper_front + 1):
        if number == lower_front and number == upper_front:
            if lower_back <= number and number <= upper_back:
                invalid_ids.append(str(number) + str(number))
                continue
        if number == lower_front and number != upper_front:
            if lower_front >= lower_back:
                invalid_ids.append(str(number) + str(number))
                continue
        if number == upper_front and number != lower_front:
            if upper_front <= upper_back:
                invalid_ids.append(str(number) + str(number))
                continue
        if number != lower_front and number != upper_front:
            invalid_ids.append(str(number) + str(number))
            

        


sum = 0

for id in invalid_ids:
    print(id)
    sum += int(id)

print("sum:")
print(sum)