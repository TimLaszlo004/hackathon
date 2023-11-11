
def cardMaker(n):
    matrix = list()
    newCardValue = 2
    maxed = n+(n-1)*(n-1)
    step = 0 # the step for generating combinations (ax from f(x) = ax+b linear equation)
    done = 0 # the number for generating combinations for different init indexes (b from f(x) = ax+b linear equation)
    for i in range(maxed):
        print(str(i+1) + " - ", end='')
        if i < n: # generate the first n card (and matrix for later purposes)
            card = list()
            matElement = list()
            for x in range(n):
                if x == 0:
                    card.append(1)
                else:
                    card.append(newCardValue)
                    matElement.append(newCardValue)
                    newCardValue += 1
            print(card)
            matrix.append(matElement)
        else: # generate all other cards (from existing values)
            complexcard = list()
            complexcard.append(step+2)
            for x in range(n-1):
                complexcard.append(matrix[x+1][(x*step+done)%(n-1)])
            done += 1
            if done == n-1:
                step += 1
                done = 0
            print(complexcard)

number = 0
file = open('input.txt', 'r')

# calculations are performed while reading the file: no need to store the whole file
while True:
    line = file.readline()
    
    if line == "":
        break
    if not line:
        break
    word = line.split()
    print(word[0])

    try:
        number = int(line)
        cardMaker(number)
    except:
        print("invalid")
      
    print()

file.close()