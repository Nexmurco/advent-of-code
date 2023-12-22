def pullIntFromText(string):
    #look for zero, one, two, three, four, five, six, seven, eight, nine
    
    #will it matter that some start and end with same letter?
    #example: eightwo should this not be considered a two? I will count it
    #Answer: the challenge agrees the two should be counted
    
    #three char nums
    if len(string) >= 3:
        string3 = string[:3]
        if string3 == "one":
            return 1
        elif string[:3] == "two":
            return 2
        elif string[:3] == "six":
            return 6
    
    if len(string) >= 4:
        if string[:4] == "four":
            return 4
        elif string[:4] == "five":
            return 5
        elif string[:4] == "nine":
            return 9
        elif string[:4] == "zero":
            return 0
        
    if len(string) >= 5:
        if string[:5] == "three":
            return 3
        elif string[:5] == "seven":
            return 7
        elif string[:5] == "eight":
            return 8
    return None

with open("D:\\Code\\Advent of Code 2023\\Dec1\\Part2\\input.txt", "r") as file:
    sum = 0
    for line in file:
        print()
        print(line)
        first = True
        for i in range(len(line)):
            if line[i:i+1].isdigit():
                if first:
                    firstDigit = int(line[i:i+1])
                    first = False
                lastDigit = int(line[i:i+1])
            else:
                if i+3 < len(line):
                    endValue = min(i+5, len(line))
                    pulledInt = pullIntFromText(line[i:endValue])
                    if pulledInt is not None:
                        if first:
                            firstDigit = pulledInt
                            first = False
                        lastDigit = pulledInt
        
        print(str(firstDigit) + str(lastDigit))
        sum += firstDigit * 10
        sum += lastDigit

print("Sum = " + str(sum))
        