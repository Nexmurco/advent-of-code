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
        row = input.rstrip('\n')
        table.append(row[::-1])

operator_indeces = []
index = 0
for char in table[len(table)-1]:
    if char == "+" or char == "*":
        operator_indeces.append(index)
    index += 1

col_start = 0
values = []
operators = []
for col_end in operator_indeces:
    numbers = []
    for row in range(len(table) - 1):
        numbers.append(table[row][col_start:col_end+1])
    values.append(numbers)
    operators.append(table[len(table)-1][col_end])
    col_start = col_end + 2

octopus_values = []
for value_set in values:
    octopus_value_set = []
    for digit in range(len(value_set[0])):
        val = ""
        for value_index in range(len(value_set)):
            val += value_set[value_index][digit]
        octopus_value_set.append(int(val.strip()))
    octopus_values.append(octopus_value_set)

grand_total = 0
for i in range(len(operators)):
    op = operators[i]
    if op == "+":
        grand_total += sum(octopus_values[i])
    if op == "*":
        grand_total += product(octopus_values[i])

print(grand_total)