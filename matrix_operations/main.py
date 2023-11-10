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
arrlist = list()
lastBetu = ""
matdict = dict()
partCalculate = False
while True:

    line = file.readline()
    
    if line == "":
      break
    if not line:
      break
    
    x = line.split()
    if len(x) == 1 and len(x[0])==1: #betu
      if lastBetu != "":
        matdict[lastBetu] = arrlist
        arrlist = list()
      lastBetu = x[0]
    elif len(x) == 1 and x[0]=="operations":
      matdict[lastBetu] = arrlist
      partCalculate = True
    elif len(x) > 1:
      if not partCalculate:
        arr = list()
        for i in range(len(x)):
          arr.append(int(x[i]))
        arrlist.append(arr)

      else:
        reslist = list()
        mulcounter = 0
        result = 0
        for i in x:
          print(i, end=' ')
        print()
        for i in range(len(x)):
          if x[i]=='*':

            reslist.append(mult(matdict[x[i-1]], matdict[x[i+1]]))

            f = i
            while f+2 < len(x):
              f += 2
              if x[f]=='*':
                reslist[-1] = mult(reslist[-1], x[f+1])
              else:
                break
        for i in range(len(x)):
          if x[i]=='+':
            if result == 0:
              if i == 1:
                result = matdict[x[i-1]]
              else:
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
          for x in i:
            print(x, end=' ')
          print()
        print()
    

 
file.close()
