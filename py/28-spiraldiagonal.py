size = 1001 #Must be odd
start = 1

grid = []
for row in range(size):
    grid.append([None]*size)
grid[size//2][size//2]=start

coords = [size//2,size//2]
direction = 'r'
for i in range(size**2):
    if direction == 'r':
        coords[1]+=1

        try:
            grid[coords[0]][coords[1]] = grid[coords[0]][coords[1]-1]+1
            if grid[coords[0]+1][coords[1]] is None:
                direction = 'd'
        except:
            pass #To catch the end of the loop

    elif direction == 'd':
        coords[0] += 1
        grid[coords[0]][coords[1]] = grid[coords[0]-1][coords[1]]+1
        if grid[coords[0]][coords[1]-1] is None:
            direction = 'l'
        
    elif direction == 'l':
        coords[1] -= 1
        grid[coords[0]][coords[1]] = grid[coords[0]][coords[1]+1]+1
        if grid[coords[0]-1][coords[1]] is None:
            direction = 'u'
        
    elif direction == 'u':
        coords[0] -= 1
        grid[coords[0]][coords[1]] = grid[coords[0]+1][coords[1]]+1
        if grid[coords[0]][coords[1]+1] is None:
            direction = 'r'
        
total = 0
selection = 0
for row in grid:
    total += row[selection]+row[-selection-1]
    selection+=1
total -= start

print(total)