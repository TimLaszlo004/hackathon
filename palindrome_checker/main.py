
import re

def formatString(word):
    return (re.sub(r'[^a-zA-Z0-9]', '', word)).casefold()

def palindromize(word):
    unique = list()
    length = len(word)//2
    if len(word)%2==1:
        length += 1
    for i in range(length):
        if word[i] != word[-i-1]:
            return -1
        else:
            unique.append(word[i])
    un = set(unique)
    return len(un)


file = open('input.txt', 'r')


while True:

    line = file.readline()
    
    if line == "":
        break
    if not line:
        break
    
    word = formatString(line)
    result = palindromize(word)
    if(result != -1):
        print("YES" + ", " + str(result))
    else:
        print("NO" + ", " + str(result))

 
file.close()
