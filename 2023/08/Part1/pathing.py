with open("D:\\Code\\Advent of Code 2023\\DEC08\\Part1\\input.txt", "r") as file:
    lines = list(file)
    instructions = lines[0].rstrip("\n")
    
    count = 0
    lrMap = {}
    firstKey = None
    for line in lines:
        count += 1
        if count <= 2:
            continue
        line = line.rstrip("\n")
        line = line.replace("= (", "").replace(",","").replace(")","")
        
        vals = line.split(" ")
        lrMap[vals[0]] = {"L":vals[1], "R":vals[2]}
        if count == 3:
            firstKey = vals[0]
        
    for key in lrMap.keys():
        print(key + ": " + lrMap[key]["L"] + ", " + lrMap[key]["R"])


    warpDriveMap = {}
    for key in lrMap.keys():
        keyInit = key
        keyCur = key
        for i in instructions:
            keyCur = lrMap[keyCur][i]
        warpDriveMap[keyInit] = keyCur

    print("warp drive map")
    for key in warpDriveMap.keys():
        print(key + " -> " + warpDriveMap[key])


    terminator = "ZZZ"
    firstKey = "AAA"

    steps = 0
    i = 0
    curKey = firstKey
    while curKey != terminator:
        steps += 1
        curI = instructions[i]
        curKey = warpDriveMap[curKey]
        i += 1
        if i >= len(instructions):
            i = 0
        if steps %1000 == 0:
            print(steps)
    
    print("warp drive distance: " + str(steps))
    print("steps: " + str(steps * len(instructions)))
    

