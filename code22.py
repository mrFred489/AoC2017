f = open("data22.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

def addLayer(grid):
    for i in range(len(grid)):
        grid[i] = ["."] + grid[i] + ["."]
    grid.insert(0, ["." for _ in range(len(grid[0]))])
    grid.append(["." for _ in range(len(grid[0]))])

    
direction = 1


for i in range(200):
    addLayer(grid)

grid2 = []

for i in grid:
    grid2.append(i.copy())
    
half = len(grid)//2

x = half
y = half


left = {
    0: 1,
    1: 2,
    2: 3,
    3: 0
}

right = {
    0: 3,
    3: 2,
    2: 1,
    1: 0
}

move = [(1,0), (0,-1), (-1, 0), (0, 1)]

c = 0

print(grid[y][x])
grid[y][x] = "X"

for i in range(10000):
    if grid[y][x] in "#I":
        direction = right[direction]
        grid[y][x] = "."
    else:
        direction = left[direction]
        grid[y][x] = "I"
        c += 1
    dx, dy = move[direction]
    x += dx
    y += dy
    if i % 1000 == 0: 
        print(i)

counter = 0

for i in grid:
    counter += i.count("I")


print(x,y)
print("part1:", c)
print(len(grid))



print("x", [str(i)[-1] for i in range(25)])


reverse = [2,3, 0, 1]

x, y = half, half

c = 0

grid = grid2

print("part2: ", c)
for i in range(25):
    print(i, grid[half - 12 + i][half-12:half+12])


for i in range(10000000):
    if grid[y][x] in "#":
        direction = right[direction]
        grid[y][x] = "F"
    elif grid[y][x] in ".":
        direction = left[direction]
        grid[y][x] = "W"
    elif grid[y][x] in "W":
        grid[y][x] = "#"
        c += 1
    elif grid[y][x] in "F":
        direction = reverse[direction]
        grid[y][x] = "."
    else: print("Fejl", grid[y][x])
    dx, dy = move[direction]
    x += dx
    y += dy
    if i % 1000000 == 0: 
        print(i)

print("part2: ", c)
for i in range(25):
    print(i, grid[half - 12 + i][half-12:half+12])
# 2511873
    
