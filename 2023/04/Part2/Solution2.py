with open("D:\\Code\\Advent of Code 2023\\Dec4\\Part2\\input.txt", "r") as file:
    sum = 0
    cards = {}
    wonCards = {}
    count = 0
    lines = list(file)

    for i in range(1, len(lines)+1):
        wonCards[i] = 1

    for line in lines:
        count += 1


        line = line.rstrip("\n")
        numbers = line.split(" | ")
        winners = numbers[0]
        guesses = numbers[1]
        winners = winners.split(": ")[1]
        winners = winners.split(" ")
        guesses = guesses.split(" ")
        g = set()
        w = set()


        g.update(guesses)
        w.update(winners)
        g.discard("")
        w.discard("")
        cards[count] = {"winners": w, "guesses": g}
        
        matches = 0
        for guess in g:
            if guess in w:
                print("match on " + guess)
                matches +=1
        
        #for every match, add won cards multiplied by the amount we have in our map
        #do this for the next number of cards equal to matches we have

        for i in range(1, matches+1):
            if count+i not in wonCards.keys():
                wonCards[count+i] = 0
            wonCards[count+i] += wonCards[count]

    print(wonCards)
    for key in wonCards.keys():
        sum += wonCards[key]

    print(sum)