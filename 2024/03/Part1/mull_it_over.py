import re

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\03\\Input\\input_test.txt", "r") as file:
    
    sum = 0
    
    for line in file:
        print(line)
        multiplications = re.findall("do\\(\\)|don't\\(\\)|mul\\(\\d{1,3}\\,\\d{1,3}\\)", line)
        print(multiplications)

        for m in multiplications:
            print(m)
            m = m.replace("mul(", "")
            m = m.replace(")", "")
            values = m.split(",")
            product = 1
            for v in values:
                product *= int(v)

            sum += product

    print("-----------")
    print("sum: " + str(sum))
    