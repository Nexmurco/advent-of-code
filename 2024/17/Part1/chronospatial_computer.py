def bitwise_xor(val1, val2):
    return val1 ^ val2

def adv(operand):
    global reg_a
    operand = get_combo_operand(operand)
    reg_a = int(reg_a / (2**operand))
    return

def bxl(operand):
    global reg_b
    reg_b = bitwise_xor(reg_b, operand)
    return

def bst(operand):
    global reg_b
    reg_b = get_combo_operand(operand) % 8
    return

def jnz(operand):
    global reg_a
    global instruction_pointer
    global skip_increment

    if reg_a == 0:
        return
    instruction_pointer = operand
    skip_increment = True
    return

def bxc(operand):
    global reg_b
    global reg_c
    reg_b = bitwise_xor(reg_b, reg_c)
    return

def out(operand):
    global outs
    outs.append(get_combo_operand(operand) % 8)
    return

def bdv(operand):
    global reg_a
    global reg_b
    operand = get_combo_operand(operand)
    reg_b = int(reg_a / (2**operand))
    return

def cdv(operand):
    global reg_a
    global reg_c
    operand = get_combo_operand(operand)
    reg_c = int(reg_a / (2**operand))
    return


def get_combo_operand(o):
    global reg_a
    global reg_b
    global reg_c

    if 0 <= o and o <= 3:
        return o
    elif o == 4:
        return reg_a
    elif o == 5:
        return reg_b
    elif o == 6:
        return reg_c
    
    return None

instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\17\\Input\\input.txt", "r") as file:
    reg_a = ""
    reg_b = ""
    reg_c = ""
    program = []
    outs = []
    line_count = 0

    for line in file:
        line = line.rstrip("\n")

        if line_count == 0:
            line = line.replace("Register A: ", "")
            reg_a = int(line)
        elif line_count == 1:
            line = line.replace("Register B: ", "")
            reg_b = int(line)
        elif line_count == 2:
            line = line.replace("Register C: ", "")
            reg_c = int(line)
        elif line_count == 3:
            pass    
        elif line_count == 4:
            line = line.replace("Program: ", "")
            inputs = line.split(",")
            for i in inputs:
                program.append(int(i))
        line_count += 1

    print(reg_a)
    print(reg_b)
    print(reg_c)
    print(program)


    instruction_pointer = 0
    pointer_increment = 2
    skip_increment = False

    while True:
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]


        function = instructions[opcode]
        function(operand)

        #increment the pointer
        if not skip_increment:
            instruction_pointer += pointer_increment
        else:
            skip_increment = False

        if instruction_pointer >= len(program) - 1:
            break



    output = ""

    for o in outs:
        output += str(o) + ","

    output = output.rstrip(",")
    print()
    print("output: " + str(output))