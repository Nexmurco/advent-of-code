from math import lcm

with open("D:\\Code\\Advent of Code 2023\\DEC08\\Part1\\input.txt", "r") as file:
    lines = list(file)
    instructions = lines[0].rstrip("\n")
    paths = {}
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
        if vals[0][2] == "A":
            paths[vals[0]] = vals[0]

    
            
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

    answerFile = open("warpdrive.txt", "w")
    for key in warpDriveMap.keys():
        print(key + " -> " + warpDriveMap[key])
        answerFile.write(key + " -> " + warpDriveMap[key] + "\n")
    answerFile.close()

    terminate = False

    loopFoundMap = {}
    loopLengthMap = {}

    for path in paths.keys():
        print("Starting Path: " + path + " " + paths[path])
        loopFoundMap[path] = False
        loopLengthMap[path] = None

    

    warpsteps = 0
    while not terminate:
        warpsteps += 1
        for path in paths.keys():
            key = paths[path]
            paths[path] = warpDriveMap[key]


        #check if we can stop yet
        terminate = True

        for path in paths.keys():
            
            if paths[path][2] == "Z" and loopFoundMap[path] == False:
                loopFoundMap[path] = True
                loopLengthMap[path] = warpsteps
                print(path + " reached " + paths[path] + " on warpstep: " + str(warpsteps))

            
        terminate = True
        for isFound in loopFoundMap.values():
            if isFound == False:
                terminate = False
        
    
    for path in loopLengthMap.keys():
        print(path + ": " + str(loopLengthMap[path]))

    multiple = 1
    for val in loopLengthMap.values():
        multiple = lcm(multiple, val)
    print(multiple)

    print(multiple * len(instructions))
    #find LCM of lengths

