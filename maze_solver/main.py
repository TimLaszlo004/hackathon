# def pather(mat, current, end, cools, beenthere):
#   # if current in beenthere:
#   #   return None
#   cools.append(current)
#   mat[current[0]][current[1]] = "#"
#   beenthere.append(mat[current[0]][current[1]])
#   if current == end:
#     return cools
#   else:
#     neighbours = []
#     if mat[current[0]-1][current[1]] != '#':
#       neighbours.append((current[0]-1, current[1]))
#     if mat[current[0]+1][current[1]] != '#':
#       neighbours.append((current[0]+1, current[1]))
#     if mat[current[0]][current[1]-1] != '#':
#       neighbours.append((current[0], current[1]-1))
#     if mat[current[0]][current[1]+1] != '#':
#       neighbours.append((current[0], current[1]+1))
    
#     if len(neighbours) == 0:
#       return None
    
#     reslist = []
#     for i in neighbours:
#       mat_copy = mat.copy()
#       cools_copy = cools.copy()
#       beenthere_copy = beenthere.copy()
#       res = pather(mat_copy, i, end, cools_copy, beenthere_copy)
#       if res is not None:
#         reslist.append(res)
    
#     if len(reslist) == 0:
#       return None
#     return min(reslist)

def pather(mat, current, end, cools):
    cools.append(current)
    mat[current[0]][current[1]] = "#"

    if current == end:
        return cools
    else:
        neighbours = []
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
        for i in neighbours:
            # Create copies of cools and mat
            cools_copy = cools.copy()
            mat_copy = [row[:] for row in mat]
            
            res = pather(mat_copy, i, end, cools_copy)
            if res is not None:
                reslist.append(res)

        if len(reslist) == 0:
            return None
        return min(reslist, key=len)


def directionChecker(route):
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
      


matrix = list()
start = (0, 0)
end = (0, 0)

file = open('input.txt', 'r')

while True:
    line = file.readline()
    
    if line == "":
      break
    if not line:
      break
    info = line.split()
    if len(info) == 1:
      # print(matrix)
      if(len(matrix) > 0):
        # coolroute = findpath(matrix, start, start, end)
        coolroute = []
        temp1 = []
        coolroute = pather(matrix, start, end, coolroute)
        directionChecker(coolroute)
        print()
      print(info[0])
      matrix = list()
    else:
      for i in range(len(info)):
        if info[i] == 'S':
          start = (len(matrix), i)
        elif info[i] == 'G':
          end = (len(matrix), i)
      matrix.append(info)
lastroute = []
temp2 = []
# lastroute = findpath(matrix, start, start, end)
lastroute = pather(matrix, start, end, lastroute)
directionChecker(lastroute)

 
file.close()