import math
with open("D:\\Code\\Advent of Code 2023\\Dec6\\Part1\\input.txt", "r") as file:

    lines = list(file)
    times = lines[0].replace("Time: ","").rstrip("\n")
    times = times.split(" ")
    theTime = ""
    for t in times:
        theTime += t

    dists = lines[1].replace("Distance: ","")
    dists = dists.split(" ")
    theDistance = ""
    for d in dists:
        theDistance += d


    product = 1

    for i in range(1):
        distance = int(theDistance)
        time = int(theTime)

        victories = 0
        
        for t in range(time):
            d = t * (time-t)
            if d > distance:
                t1 = t
                print("t1: " + str(t1))
                break
        
        for t in range(time, 0, -1):
            d = t * (time-t)
            if d > distance:
                t2 = t
                print("t2: " + str(t2))
                break

        victories = t2 - t1
        print("victories: " + str(victories))
        
        
        product *= victories
        print(product)

        #47, 30, 24, 20

        
    
