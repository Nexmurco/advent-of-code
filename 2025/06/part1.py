import sys
import re
input_file = sys.argv[1]

def sum(values):
    sum = 0
    for v in values:
        sum += v
    return sum

def product(values):
    sum = 1
    for v in values:
        sum *= v
    return sum

table = []
with open(input_file, "r") as input_lines:
    for input in input_lines:
        values = re.split(r'[\s]+', input.strip())
        table.append(values)


operator_index = len(table) - 1
grand_total = 0

for col in range(len(table[0])):
    values = []
    operator = None
    for row in range(len(table)):
        value = table[row][col]
        if row == operator_index:
            operator = value
        else:
            values.append(int(value))
    
    if operator == "+":
        grand_total += sum(values)
    elif operator == "*":
        grand_total += product(values)

print(grand_total)