from dataclasses import dataclass

@dataclass
class Machine:
    a: tuple
    b: tuple
    prize: tuple


with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\13\\Input\\input.txt", "r") as file:
    print("open")
    count = 0
    machine_id = 0
    machines = {}

    sum = 0

    a = (-1,-1)
    b = (-1,-1)
    prize = (-1,-1)

    for line in file:
        mod = count % 4
        line = line.rstrip("\n")
        
        if mod == 0:
            #button a
            line = line.replace("Button A: X+", "")
            line = line.replace("Y+", "")
            inputs = line.split(", ")
            
            a = (int(inputs[0]), int(inputs[1]))

        elif mod == 1:
            #button b
            line = line.replace("Button B: X+", "")
            line = line.replace("Y+", "")
            inputs = line.split(", ")
            
            b = (int(inputs[0]), int(inputs[1]))
        elif mod == 2:
            #prize
            line = line.replace("Prize: X=", "")
            line = line.replace("Y=", "")
            inputs = line.split(", ")

            prize = (int(inputs[0]), int(inputs[1]))
        elif mod == 3:
            #next machine
            machines[machine_id] = Machine(a, b, prize)
            machine_id += 1

        count += 1

    cost_a = 3
    cost_b = 1

    for machine in machines.values():
        #find if there is a possible combination of values to produce prize's x
        print()
        print("finding x coefficients of machine ")
        print(str(machine))
        x1 = machine.a[0]
        x2 = machine.b[0]
        xf = machine.prize[0]
        
        c1 = -1

        coefficients_x = []
        while c1 * x1 <= xf:
            c1 += 1
            #check if the sum of c1*x1 and c2*x2 = xf
            t1 = c1 * x1
            if t1 == xf:
                coefficients_x.append((c1, 0))
                continue
            elif t1 < xf:
                #get t2
                t2 = xf - t1
                if t2 % x2 == 0:
                    c2 = int(t2 / x2)
                    coefficients_x.append((c1, c2))
                else:
                    continue
        
        coefficients = []

        print("x coefficients: ")
        print(coefficients_x)

        for cx in coefficients_x:
            if ((cx[0] * machine.a[1]) + (cx[1] * machine.b[1])) == machine.prize[1]:
                coefficients.append((cx[0], cx[1]))
        
        print("matching coefficients: ")
        print(str(coefficients))
        
        min_cost = None
        for c in coefficients:
            tokens = (cost_a * c[0]) + (cost_b * c[1])
            if min_cost is None or tokens < min_cost:
                print("new least cost: ")
                print(str(c) + " at price of " + str(tokens))
                min_cost = tokens
        
        if min_cost is not None:
            sum += min_cost
    
    print(sum)

            