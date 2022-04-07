#In Progress

grid = []
size = 2
paths = 0
prevpath = [] #True is right, False is down

for i in range(size):
    row = []
    for k in range(size):
       row.append([i,k])
    grid.append(row)
del row

for i in range(size**2):
    curpath = []
    if prevpath == []:
        for k in range(size):
            curpath.append(True)
        for k in range(size):
            curpath.append(False)
    prevpath = curpath
    print(prevpath)