with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        print(line)
        first = True
        for char in line:
            if char.isdigit():
                if first:
                    firstDigit = int(char)
                    first = False
                lastDigit = int(char)

        print(line)
        print(firstDigit)
        print(lastDigit)
        print()    
        sum += 10*firstDigit
        sum += lastDigit

print("Sum = " + str(sum))
        