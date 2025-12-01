import sys
input_file = sys.argv[1]

pos = 50
prev_pos = pos
count = 0

with open(input_file, "r") as input:

    for line in input:
        line = line.rstrip()

        #extract direction from line
        if line[:1] == "L":
            dir = -1
        else:
            dir = 1

        #keep the prev pos and get the new pos
        prev_pos = pos
        pos = pos + (int(line[1:]) * dir)

        
        count_increase = abs((pos//100) - (prev_pos//100))
        
        #negative case
        if dir < 0:
            #if we end on a multiple of 100, integer division into subtraction will fail to catch it
            if pos % 100 == 0:
                count_increase += 1
            #if we start on a multiple of 0, we double count, so remove the double count
            if prev_pos % 100 == 0:
                count_increase -= 1
        
        count += count_increase
        
print("password: " + str(count))