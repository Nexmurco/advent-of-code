import re

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\03\\Input\\input.txt", "r") as file:
    
    sum = 0

    enable_multiplication = True
    
    for line in file:
        commands = re.findall("do\\(\\)|don't\\(\\)|mul\\(\\d{1,3}\\,\\d{1,3}\\)", line)


        for c in commands:
            product = 0
            if c == "do()":
                enable_multiplication = True
            elif c == "don't()":
                enable_multiplication = False
            elif enable_multiplication:
                c = c.replace("mul(", "")
                c = c.replace(")", "")
                values = c.split(",")
                product = 1
                for v in values:
                    product *= int(v)

            sum += product

    print("-----------")
    print("sum: " + str(sum))
    