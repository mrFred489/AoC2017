f = open("data19.txt")

data = []

for line in f:
    data.append(line.strip("\n"))

y = 0

x = data[0].index("|")

done = False

direction = "down"

relevant = "|-+"

res = ""

dirs = {
    "up": (-1,0),
    "rigth": (0,1),
    "down": (1,0),
    "left": (0,-1),
}

perpe = {
    "up": ((0,-1, "left"), (0,1, "rigth"), "-"),
    "rigth": ((1, 0, "down"), (-1,0, "up"), "|"),
    "down": ((0,-1, "left"), (0,1, "rigth"), "-"),
    "left": ((1, 0, "down"), (-1,0, "up"), "|"),

}

count = 0

while data[y][x] != " ":
    count += 1
    if data[y][x] not in relevant:
        res += data[y][x]
    if data[y][x] == "+":
        ndir1, ndir2, stuff = perpe[direction]
        if data[y+ndir1[0]][x+ndir1[1]] == stuff:
            direction = ndir1[2]
        if data[y+ndir2[0]][x+ndir2[1]] == stuff:
            direction = ndir2[2]
    dy, dx = dirs[direction]
    x += dx
    y += dy

print(x, y)
print(res)
print(count)

