from enum import Enum

class ModType(Enum):
    FLIPFLOP = 1
    CONJUNCTION = 2
    BROADCASTER = 3

class PulseLevel(Enum):
    Low = 1
    High = 2


pulse_queue = []

with open("D:\\Code\\advent-of-code\\advent-of-code\\2023\\20\\input.txt", "r") as file:
    lines = list(file)


    modules = {}

    for line in lines:
        line = line.rstrip("\n")
        data = line.split(" -> ")
        m = data[0]
        destinations = data[1].split(", ")
        module = {}

        if "%" in m:
            module["type"] = ModType.FLIPFLOP
            module["destinations"] = destinations
            module["on"] = False
            key = m[1:]
        elif "&" in m:
            module["type"] = ModType.CONJUNCTION
            module["destinations"] = destinations
            module["inputs"] = {}
            key = m[1:]
        elif "broadcaster" in m:
            module["type"] = ModType.BROADCASTER
            module["destinations"] = destinations
            key = "broadcaster"
        
        modules[key] = module

    #go through each module and hook up all the inputs of the conjunctions
    
    for key in modules.keys():
        print("---")
        print(" -" + str(key))
        print("---")
        for dest in modules[key]["destinations"]:
            print(dest)
            if dest in modules.keys():
                submod = modules[dest]
                if submod["type"] == ModType.CONJUNCTION and key not in submod["inputs"].keys():
                    submod["inputs"][key] = PulseLevel.Low
    print()
    for key in modules.keys():
        print(key)
        print(modules[key])


    count_low = 0
    count_high = 0

    for i in range(1000):

        pulse_queue.append({"dest": "broadcaster", "level": PulseLevel.Low, "source": "button"})
        
        while len(pulse_queue) > 0:
            pulse = pulse_queue.pop(0)

            if pulse["level"] == PulseLevel.Low:
                count_low += 1
            else:
                count_high += 1

            if pulse["dest"] in modules:
                module = modules[pulse["dest"]]
            else:
                continue

            if module["type"] == ModType.BROADCASTER:
                for d in module["destinations"]:
                    pulse_queue.append({"dest": d, "level": pulse["level"], "source": pulse["dest"]})
            elif module["type"] == ModType.CONJUNCTION:
                #update input tracking
                module["inputs"][pulse["source"]] = pulse["level"]

                #check if there are any low pulses
                pulse_level = PulseLevel.Low
                for input in module["inputs"].values():
                    if input == PulseLevel.Low:
                        pulse_level = PulseLevel.High
                        break
                
                for input in module["destinations"]:
                    pulse_queue.append({"dest": input, "level": pulse_level, "source": pulse["dest"]})
            elif module["type"] == ModType.FLIPFLOP and pulse["level"] == PulseLevel.Low:
                if module["on"] == True:
                    module["on"] = False
                    pulse_level = PulseLevel.Low
                else:
                    module["on"] = True
                    pulse_level = PulseLevel.High

                for input in module["destinations"]:
                        pulse_queue.append({"dest": input, "level": pulse_level, "source": pulse["dest"]})
    
    print("done")
    print(count_low)
    print(count_high)
    print(count_high * count_low)
