def isIncreasing(val1, val2):
    return val2 > val1

def isValidDifference(val1, val2):
    diff = abs(val1 - val2)
    return (diff >= 1) and (diff <= 3)

def checkReport(values):
    prevIncreasing = None
    prevValue = int(values[0])
    isValid = True
    
    for index in range(1, len(values)):
        currValue = int(values[index])
        currIncreasing = isIncreasing(currValue, prevValue)
        if (index != 1) and (currIncreasing != prevIncreasing):
            isValid = False
            break
        elif not isValidDifference(currValue, prevValue):
            isValid = False
            break
        
        prevValue = currValue
        prevIncreasing = currIncreasing

    return isValid

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\02\\Input\\input.txt", "r") as file:
    sum = 0
    count = 0
    for line in file:
        count += 1

        line = line.rstrip("\n")
        values = line.split()
        
        if checkReport(values):
            sum += 1
        else:
            for index in range(0, len(values)):
                subValues = values.copy()
                subValues.pop(index)
                if(checkReport(subValues)):
                    sum += 1
                    break

    print("-----------")
    print("sum: " + str(sum))