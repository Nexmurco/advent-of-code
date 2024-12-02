def isIncreasing(val1, val2):
    return val2 > val1

def isValidDifference(val1, val2):
    diff = abs(val1 - val2)
    return (diff >= 1) and (diff <= 3)


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\02\\Input\\input.txt", "r") as file:
    sum = 0
    
    for line in file:
        line = line.rstrip("\n")
        values = line.split()

        isValidReport = True

        prevIncreasing = None
        prevValue = int(values[0])

        for index in range(1, len(values)):
            currValue = int(values[index])
            currIncreasing = isIncreasing(currValue, prevValue)
            if (index != 1) and (currIncreasing != prevIncreasing):
                isValidReport = False
                break
            if not isValidDifference(currValue, prevValue):
                isValidReport = False
                break
            
            prevValue = currValue
            prevIncreasing = currIncreasing

        if isValidReport:
            sum += 1

    print("-----------")
    print("sum: " + str(sum))
    