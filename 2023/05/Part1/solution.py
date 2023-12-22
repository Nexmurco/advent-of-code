def intervalCompression(keepInterval, additionalInterval):
    useLower = False
    useUpper = False
    if additionalInterval[0] < keepInterval[1] and additionalInterval[0] > keepInterval[0]:
        useLower = True

    if additionalInterval[1] < keepInterval[1] and additionalInterval[1] > keepInterval[0]:
        useUpper = True
    
    intervals = []
    if useLower:
        intervals.append((keepInterval[0], additionalInterval[0]-1))
        if useUpper:
            intervals.append((additionalInterval[0], additionalInterval[1]))
            intervals.append((additionalInterval[1]+1, keepInterval[1]))
        else:
            intervals.append((additionalInterval[0], keepInterval[1]))
    elif useUpper:
        intervals.append((keepInterval[0], additionalInterval[1]))
        intervals.append((additionalInterval[1]+1,keepInterval[1]))
    else:
        intervals.append(keepInterval)

    return intervals



with open("D:\\Code\\Advent of Code 2023\\Dec5\\Part1\\input.txt", "r") as file:
    minLocation = None
    lines = list(file)
    #print(lines)
    curMap = None
    seedList = []
    seedSoilMap = {}
    soilFertilizerMap = {}
    fertilizerWaterMap = {}
    waterLightMap = {}
    lightTempMap = {}
    tempHumidityMap = {}
    humidityLocationMap = {}
    mapMap = {"seedSoilMap": seedSoilMap, "soilFertilizerMap": soilFertilizerMap, "fertilizerWaterMap": fertilizerWaterMap, "waterLightMap":waterLightMap, "lightTempMap":lightTempMap, "tempHumidityMap":tempHumidityMap, "humidityLocationMap":humidityLocationMap}

    for line in lines:
        line = line.rstrip("\n")

        if line.find("seeds:") != -1:
            line = line.replace("seeds: ", "")
            seeds = line.split(" ")
            for i in range(0, len(seeds), 2):
                seedList.append((int(seeds[i]), int(seeds[i])+int(seeds[i+1])-1))

            print(seedList)
    
        elif line.find("seed-to-soil map:") != -1:
            curMap = seedSoilMap
        elif line.find("soil-to-fertilizer map:") != -1:
            curMap = soilFertilizerMap
        elif line.find("fertilizer-to-water map:") != -1:
            curMap = fertilizerWaterMap
        elif line.find("water-to-light map:") != -1:
            curMap = waterLightMap
        elif line.find("light-to-temperature map:") != -1:
            curMap = lightTempMap
        elif line.find("temperature-to-humidity map:") != -1:
            curMap = tempHumidityMap
        elif line.find("humidity-to-location map:") != -1:
            curMap = humidityLocationMap
        else:
            if line != "":
                #split input into 3 parts
                numbers = line.split(" ")
                rangeSource = (int(numbers[1]), int(numbers[1])+int(numbers[2]))
                rangeDestination = (int(numbers[0]), int(numbers[0])+int(numbers[2]))
                curMap[rangeSource] = rangeDestination
        
    
    seedIOList = []
    for seedRange in seedList:
        seedIOList.append({"input":seedRange, "output":seedRange})
    
    print(seedIOList)

    for map in mapMap.keys():
        print("Compressing map: " + str(map))
        print(mapMap[map])
        for input in mapMap[map].keys():
            newSeedIOs = []
            for seedIO in seedIOList:
                intervals = intervalCompression(seedIO["output"], input)
                #get jump value between input and output of seedIO
                jump = seedIO["output"][0] - seedIO["input"][0]
                
                first = True
                for interval in intervals:
                    if first:
                        first = False
                        seedIO["output"] = interval
                        seedIO["input"] = (interval[0]-jump, interval[1]-jump)
                    else:
                        newSeedIO = {"output": interval, "input":(interval[0]-jump, interval[1]-jump)}
                        newSeedIOs.append(newSeedIO)

            for newSeedIO in newSeedIOs:    
                seedIOList.append(newSeedIO)
        
        #pass in the outputs of each seedIO into the current map and adjust their values based on map outputs
        for seedIO in seedIOList:
            output = seedIO["output"]
            for inputRange in mapMap[map].keys():
                if output[0] >= inputRange[0] and output[1] <= inputRange[1]:
                    jump0 = output[0] - inputRange[0]
                    jump1 = output[1] - inputRange[0]
                    outputRange = mapMap[map][inputRange]
                    seedIO["output"] = (outputRange[0] + jump0, outputRange[0]+jump1)
        
        print("updated Seed IO List:")
        print(seedIOList)

    #sweep through intervals and find lowest value

    outputVal = None

    for seedIO in seedIOList:
        oVal = seedIO["output"][0]
        if outputVal is None:
            outputVal = oVal
        elif oVal < outputVal:
            outputVal = oVal

    print("lowest value: " + str(outputVal))
                


        
        
    #for map in mapMap:
        #print(map)
        #print(mapMap[map])
        #print()

    #print(seedList)
    # for seed in seedList:
    #     #print()
    #     value = int(seed)
    #     #print("Seed: " + str(seed))
    #     for map in mapMap.keys():
    #         #print(map + ": " + str(value))
    #         for key in mapMap[map].keys():
    #             if value >= key[0] and value <= key[1]:
    #                 jump = value - key[0]
    #                 value = mapMap[map][key][0] + jump
    #                 break
    #     if minLocation is None:
    #         minLocation = value
    #     else:
    #         if value < minLocation:
    #             minLocation = value
    #     #print("Location: " + str(value))
    # print()
    # print("Closest Location: " + str(minLocation))


    
