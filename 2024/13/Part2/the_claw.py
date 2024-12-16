from dataclasses import dataclass

@dataclass
class Machine:
    a: tuple
    b: tuple
    prize: tuple


def cost(pair):
    cost_a = 3
    cost_b = 1
    return (cost_a * pair[0]) + (cost_b * pair[1])

with open("C:\\Users\\perki\\Documents\\GitHub\\advent-of-code\\2024\\13\\Input\\input_test.txt", "r") as file:
    #print("open")
    count = 0
    machine_id = 0
    machines = {}

    sum = 0

    a = (-1,-1)
    b = (-1,-1)
    prize = (-1,-1)

    prize_offset = 10000000000000

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

            prize = (int(inputs[0]) + prize_offset, int(inputs[1]) + prize_offset)
        elif mod == 3:
            #next machine
            machines[machine_id] = Machine(a, b, prize)
            machine_id += 1

        count += 1


    for machine in machines.values():
        #find if there is a possible combination of values to produce prize's x
        #get the lowest and highest value of c1 that produces the correct sum
        print()
        print(str(machine))
        ci = None
        c1 = 0
        while ci is None:
            t1 = c1 * machine.a[0]
            tf = machine.prize[0]
            t2 = tf - t1
            
            if t2 % machine.b[0] == 0:
                c2 = int(t2 / machine.b[0])
                ci = (c1, c2)
                break

            c1 += 1
        

        ci2 = None
        c1 = ci[0]
        while ci2 is None:
            c1 += 1

            t1 = c1 * machine.a[0]
            tf = machine.prize[0]
            t2 = tf - t1
            
            if t2 % machine.b[0] == 0:
                c2 = int(t2 / machine.b[0])
                ci2 = (c1, c2)
                break

        c_jump = (ci2[0] - ci[0], ci2[1] - ci[1])


        cf = None
        c1 = int(machine.prize[0] / machine.a[0]) + 1
        
        while cf is None:

            t1 = c1 * machine.a[0]
            tf = machine.prize[0]
            t2 = tf - t1
            
            if t2 >= 0 and t2 % machine.b[0] == 0:
                c2 = int(t2 / machine.b[0])
                cf = (c1, c2)
                break

            c1 -= 1

        print(ci)
        print(ci2)
        print(c_jump)
        print(cf)

        costs = {}

        costs[ci] = cost(ci)
        costs[ci2] = cost(ci2)
        costs[cf] = cost(cf)

        print(costs)

        #we now have the end points and the interval distance
        #we can binary search and be greedy
