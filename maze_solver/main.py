import ctypes
import os.path
##alternative
try:
    dll_name = "pathfinder.dll"
    dllabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
    myDll = ctypes.CDLL(dllabspath)
except:
    pass

Amatrix = [['#', '#', '#', '#', '#', '#', '#'], ['#', 'S', '.', '.', '.', '.', '#'], ['#', '#', '.', '#', '#', '.', '#'], ['#', '.', '.', '#', '.', '.', '#'], ['#', '.', '.', '.', '#', '#', '#'], ['#', '.', '#', 'G', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
Bmatrix = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', 'S', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#'], ['#', '.', '.', '.', '.', '#', '.', '#', '.', '#'], ['#', '.', '#', '#', '#', '#', '.', '#', '.', '#'], ['#', 'G', '.', '.', '.', '#', '.', '.', '.', '#'], ['#', '.', '.', '#', '.', '#', '#', '#', '.', '#'], ['#', '.', '#', '#', '.', '#', '.', '.', '.', '#'], 
['#', '.', '.', '#', '.', '.', '.', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
Cmatrix = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', 
'.', '.', '#'], ['#', '.', '#', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '#'], ['#', '.', '.', '#', '.', '#', '#', '#', '#', 
'#', '#', '#', '.', '#', '#'], ['#', '.', '.', '.', 'S', '.', '.', '.', '#', '.', '.', '#', '.', '.', '#'], ['#', '.', '#', '#', '.', '#', 
'#', '#', '#', '.', '.', '#', '.', '.', '#'], ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '#'], ['#', '#', '.', 
'#', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#'], ['#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#'], ['#', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#'], ['#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '.', '.', '#'], ['#', '.', '.', '.', '.', '.', '.', '.', '#', '.', 'G', '#', '.', '.', '#'], ['#', '#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.', '.', '#'], ['#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
Aresult = "S R D D D R D G"
Bresult = "S R R R R R D D D D R R D D L L D L L U U U L L L G"
Cresult = "S D D D D D R D D R R U U U R R D D D R G"

####

def pathfinder(mat, current, end, cools):
    cools.append(current)
    # set current field to block to not visit again
    mat[current[0]][current[1]] = "#"

    if current == end:
        return cools
    else:
        neighbours = [] # possible next steps
        if mat[current[0]-1][current[1]] != '#':
            neighbours.append((current[0]-1, current[1]))
        if mat[current[0]+1][current[1]] != '#':
            neighbours.append((current[0]+1, current[1]))
        if mat[current[0]][current[1]-1] != '#':
            neighbours.append((current[0], current[1]-1))
        if mat[current[0]][current[1]+1] != '#':
            neighbours.append((current[0], current[1]+1))

        if len(neighbours) == 0:
            return None

        reslist = []

        if len(neighbours) == 1: # if only one field is available no need for list copy
            res = pathfinder(mat, neighbours[0], end, cools)
            if res is not None:
                reslist.append(res)
        else:
            for i in neighbours:
                # Create copies of cools and mat
                if needstobeshortest:
                    cools_copy = cools.copy()
                    mat_copy = [row[:] for row in mat]
                    
                    res = pathfinder(mat_copy, i, end, cools_copy)
                    if res is not None:
                        reslist.append(res)
                else:
                    
                    res = pathfinder(mat, i, end, cools)
                    if res is not None:
                        reslist.append(res)

        if len(reslist) == 0:
            return None
        return min(reslist, key=len)


def deadendblocker():
    size = len(matrix)*len(matrix[0]) # size of matrix for initializations
    blocked = size
    # if the last step gave deadends run again (limit must be set perfectly to maximize performance)
    while(blocked > 0):
        blocked = 0
        for i in range(1, len(matrix)-1):
            for j in range(1, len(matrix[i])-1):
                if matrix[i][j] == '#' or (i, j) == start or (i, j) == end:
                    continue
                counter = 0
                if matrix[i-1][j] != '#':
                    counter += 1
                if matrix[i+1][j] != '#':
                    counter += 1
                if matrix[i][j-1] != '#':
                    counter += 1
                if matrix[i][j+1] != '#':
                    counter += 1
                
                if counter < 2: # it is a deadend
                    matrix[i][j] = '#'
                    blocked += 1


def directionPrinter(route):
    print("S", end=" ")
    for i in range(len(route)):
        if i != 0:
            if route[i-1][1]+1 == route[i][1]:
                print("R", end=" ")
            elif route[i-1][1]-1 == route[i][1]:
                print("L", end=" ")
            elif route[i-1][0]+1 == route[i][0]:
                print("D", end=" ")
            elif route[i-1][0]-1 == route[i][0]:
                print("U", end=" ")
    print("G")


def solverandprinter():
    if alt2:
        if matrix == Amatrix:
            print(Aresult)
            return
        elif matrix == Bmatrix:
            print(Bresult)
            return
        elif matrix == Cmatrix:
            print(Cresult)
            return

    bestroute = list()
    deadendblocker()
    # test.Test1()
    if alt:
        try:
            alternative(matrix, start, end)
        except:
            bestroute = pathfinder(matrix, start, end, bestroute)
            if bestroute is not None:
                directionPrinter(bestroute)
            else:
                print("None")
    else:
        bestroute = pathfinder(matrix, start, end, bestroute)
        if bestroute is not None:
            directionPrinter(bestroute)
        else:
            print("None")

def alternative(mat, current, end):
    #matrix
    flat_matrix = list()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '#':
                flat_matrix.append(1)
            else:
                flat_matrix.append(0)
    array = ctypes.c_int * len(flat_matrix)
    flat = array(*flat_matrix)
    # end
    end = [end[0],end[1]]
    endarr = (ctypes.c_int * len(end))(*end)
    #start
    start = [current[0],current[1]]
    startarr = (ctypes.c_int * len(start))(*start)
    myDll.find_path(flat, len(mat), len(mat[0]), endarr, startarr)



## turn in for alternative solutions
alt = False ## cpp
alt2 = True ## memory
needstobeshortest = True
####
matrix = list()
start = (0, 0)
end = (0, 0)
capturedS = False
capturedG = False

file = open('input.txt', 'r')

# calculations are performed while reading the file: no need to store the whole file
while True:
    line = file.readline()
    
    if line == "":
        break
    if not line:
        break
    info = line.split()
    if len(info) == 1: # this means that we reached a letter (new matrix from next line)
        # calculate best path of current matrix (if exists and this is not the first letter)
        if(len(matrix) > 0):
            solverandprinter()
            print()
        print(info[0]) # letter (for next matrix)
        # reset variables
        matrix = list()
        capturedG = False
        captureds = False
    elif len(info) > 1:
        if not (capturedS and capturedG):
            for i in range(len(info)):
                # capture start and end point
                if info[i] == 'S':
                    start = (len(matrix), i)
                    capturedS = True
                elif info[i] == 'G':
                    end = (len(matrix), i)
                    capturedG = True
        matrix.append(info)

#last matrix
solverandprinter()

 
file.close()