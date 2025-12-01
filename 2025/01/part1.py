import sys
input_file = sys.argv[1]

pos = 50
count = 0

with open(input_file, "r") as input:
    for line in input:
        line = line.rstrip()
        if line[:1] == "L":
            dir = -1
        else:
            dir = 1

        pos = (pos + (int(line[1:]) * dir))
        if pos % 100 == 0:
            count += 1
    
print("password: " + str(count))