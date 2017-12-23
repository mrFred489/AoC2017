f = open("data11.txt")

directions = {
    "n" : (0, -1),
    "ne" : (1, -1),
    "se" : (1, 1),
    "s" : (0, 1),
    "sw" : (-1, 1),
    "nw" : (-1,-1)
}

maxdist = 0

maxx = 0
maxy = 0

x = 0
y = 0

data = f.readline().strip().split(",")


def distance(x,y):
    return max(
        abs(y),
        abs(x),
        abs((x - y)*-1)
    )

for i in data:
    dx, dy = directions[i]
    x += dx
    y += dy
    if distance(x,y) > maxdist:
        maxdist = distance(x,y)


ret = min(abs(x), abs(y)) + (max(abs(x), abs(y))-min(abs(x), abs(y)))

print(ret)

print(maxdist)



