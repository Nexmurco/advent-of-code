def operate(i1, i2, operation):
    if operation == "XOR":
        return i1 ^ i2
    if operation == "AND":
        return i1 and i2
    if operation == "OR":
        return i1 or i2
    return None

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\24\\Input\\input.txt", "r") as file:
    is_init = True
    bin_map = {}
    operation_map = {}
    gate_map = {}
    reverse_gate_map = {}

    input_chain = {}

    resolved_inputs = set(())
    unresolved_inputs = set(())

    for line in file:
        line = line.rstrip("\n")
        if is_init:
            if line == "":
                is_init = False
            else:
                split = line.split(": ")
                bin_map[split[0]] = int(split[1])
                resolved_inputs.add(split[0])
        else:
            split = line.split(" -> ")
            op_params = split[0].split(" ")
            operation_map[(op_params[0], op_params[2])] = op_params[1]
            gate_map[(op_params[0], op_params[2])] = split[1]
            reverse_gate_map[split[1]] = (op_params[0], op_params[2])
            
            if split[1] not in bin_map:
                bin_map[split[1]] = None
                unresolved_inputs.add(split[1])
            
            if op_params[0] not in bin_map:
                bin_map[op_params[0]] = None
                unresolved_inputs.add(op_params[0])

            if op_params[2] not in bin_map:
                bin_map[op_params[2]] = None
                unresolved_inputs.add(op_params[2])


    print("resolved inputs")
    print(resolved_inputs)
    print()

    while len(unresolved_inputs) > 0:
        for unresolved_input in unresolved_inputs:

            il, ir = reverse_gate_map[unresolved_input]
            if il in resolved_inputs and ir in resolved_inputs:

                operation = operation_map[(il, ir)]
                output = operate(bin_map[il], bin_map[ir], operation)
                
                bin_map[unresolved_input] = output

                resolved_inputs.add(unresolved_input)
                unresolved_inputs.remove(unresolved_input)
                break
        
    input_list = list(resolved_inputs)
    input_list.sort()
    input_list.reverse()
    

    value = ""
    for i in input_list:
        if i[0] == "z":
            value += str(bin_map[i])

    print(value)
    print(int(value, 2))