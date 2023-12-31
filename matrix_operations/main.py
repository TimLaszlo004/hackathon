def mult(_a,_b):
    _c = [[0 for _ in range(len(_b[0]))] for _ in range(len(_a))]

    for i in range(len(_a)):
        for j in range(len(_b[0])):
            for k in range(len(_b)):
                _c[i][j] += _a[i][k] * _b[k][j]

    return _c

def add(_a,_b):
    _c = [[0 for _ in range(len(_a[0]))] for _ in range(len(_a))]

    for i in range(len(_a)):
        for x in range(len(_a[0])):
            _c[i][x] += _b[i][x] + _a[i][x]
    return _c


file = open('input.txt', 'r')
arrlist = list() # store matrix temporarily
lastBetu = "" # store matrix's letter temporarily
matdict = dict() # store matrices

isPartCalculate = False

while True:

    line = file.readline()
    
    if line == "":
      break
    if not line:
      break
    
    x = line.split()
    if len(x) == 1 and len(x[0])==1: # letter
        if lastBetu != "":
            matdict[lastBetu] = arrlist
            arrlist = list()
        lastBetu = x[0]
    elif len(x) == 1 and x[0]=="operations":
        matdict[lastBetu] = arrlist
        isPartCalculate = True
    elif len(x) > 1:
        if not isPartCalculate: # read and store matrix
            arr = list()
            for i in range(len(x)):
                arr.append(int(x[i]))
            arrlist.append(arr)

        else: # read data and perform calculation
            reslist = list()
            mulcounter = 0
            result = 0
            for i in range(len(x)):
                if i < len(x)-1:
                    print(x[i], end=' ')
                else:
                    print(x[i])
                
            for i in range(len(x)): # multiplications
                if x[i]=='*':
                    reslist.append(mult(matdict[x[i-1]], matdict[x[i+1]]))

                    f = i
                    while f+2 < len(x):
                        f += 2
                        if x[f]=='*':
                            reslist[-1] = mult(reslist[-1], x[f+1])
                        else:
                            break
            for i in range(len(x)): # additions
                if x[i]=='+':
                    if result == 0:
                        if i == 1:
                            result = matdict[x[i-1]]
                        else: # first addition element comes from multiplication
                            result = reslist[mulcounter]
                            mulcounter += 1
                    
                    if i+2<len(x):
                        if x[i+2]=='+':
                            result = add(result, matdict[x[i+1]])
                        elif x[i+2]=='*':
                            result = add(result, reslist[mulcounter])
                            mulcounter +=1
                    else:
                        result = add(result, matdict[x[i+1]])
            
            for i in result:
                for x in range(len(i)):
                    if x < len(i)-1:
                        print(i[x], end=' ')
                    else:
                        print(i[x])
            print()
    

 
file.close()
