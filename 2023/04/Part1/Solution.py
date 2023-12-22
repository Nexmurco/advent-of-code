with open("D:\\Code\\Advent of Code 2023\\Dec4\\Part1\\input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.rstrip("\n")
        numbers = line.split(" | ")
        winners = numbers[0]
        guesses = numbers[1]
        winners = winners.split(": ")[1]
        
        winners = winners.split(" ")
        matches = 0
        guesses = guesses.split(" ")

        g = set()
        w = set()

        g.update(guesses)
        w.update(winners)

        g.discard("")
        w.discard("")
        
        for guess in g:
            if guess in w:
                print("match on " + guess)
                matches +=1
        

        points = pow(2, matches-1)
        if matches == 0:
            points = 0
        sum += points
        print(matches)
    print(sum)