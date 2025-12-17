from collections import deque
import math
import sys
input_file = sys.argv[1]

def operate(state, operation):
    new_state = state.copy()
    for position in operation:
        new_state[position] = not new_state[position]
    return new_state

def construct_state_string(states):
    state_string = ""
    for state in states:
        state_string += str(state)
    return state_string
    

machines = {}

with open(input_file, "r") as input_lines:
    index = 0
    for line in input_lines:
        line = line.rstrip()

        machine = {}
        operations = []
        for element in line.split(" "):
            char_start = element[0]

            if char_start == "[":
                final = []
                for i in element[1:len(element)-1]:
                    if i == ".":
                        final.append(False)
                    else:
                        final.append(True)
                    machine["final_state"] = final
            elif char_start == "(":
                values = []
                for i in element[1:len(element)-1].split(","):
                    values.append(int(i))
                operations.append(values)
            elif char_start == "{":
                joltages = []
                for i in element[1:len(element)-1].split(","):
                    joltages.append(int(i))
                machine["joltages"] = joltages
        
        machine["operations"] = operations
        machines[index] = machine
        index += 1

#BFS search each operation
q = deque()


total = 0
#use states to hold state, and number of steps it took to get there
for key in machines:
    machine = machines[key]
    state_init = [False] * len(machine["final_state"])
    final_state_string = construct_state_string(machine["final_state"])

    state = state_init.copy()
    search = True

    best_depth = math.inf
    q.append((state, 0))

    states = {}

    print("starting " + str(key))

    while len(q) > 0:
        current_state, depth = q.popleft()
        state_string = construct_state_string(current_state)

        if depth > best_depth:
            #we have already found a faster route, end this path
            continue

        if state_string in states and states[state_string] < depth:
            #this case means we already found a faster way to this state
            continue
        
        states[state_string] = depth

        if state_string == final_state_string:
            best_depth = depth
            #if we have reached the final state, end this path
            continue


        for operation in machine["operations"]:
            #perform each operation on the current state and continue the search
            q.append((operate(current_state, operation), depth + 1))

    print("best depth: " + str(best_depth))
    total += best_depth

print(total)    