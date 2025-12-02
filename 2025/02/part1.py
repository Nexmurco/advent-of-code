import sys
input_file = sys.argv[1]

pairs = []
with open(input_file, "r") as input:
    for line in input:
        ranges = line.split(",")
        for r in ranges:
            pair = r.split("-")
            pairs.append((pair[0], pair[1]))

pairs_trimmed = []

for pair in pairs:
    #first check the number of digits in the min and max range, pull them in to be even number
    lower = pair[0]
    upper = pair[1]
    digits_lower = len(lower)
    digits_upper = len(upper)

    if digits_lower % 2 == 1:
        new_lower = 10**digits_lower
        if new_lower < int(upper):
            pair = (str(new_lower), upper)
    
    if digits_upper % 2 == 1:
        new_upper = (10**(digits_upper-1))-1
        if new_upper > int(lower):
            pair = (lower, str(new_upper))
    
    digits_lower = len(pair[0])
    digits_upper = len(pair[1])

    if digits_lower % 2 == 0 and digits_upper % 2 == 0:
        pairs_trimmed.append(pair)


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