


dance = [chr(97+i) for i in range(16)]

def rotate(l, n):
    return l[-n:] + l[:-n]

f = open("data16.txt")

data = f.readline().strip().split(",")

spin = []
exch = []
part = []

prevs = []

# for move in data:
#     if move[0] == "s":
#         dance = rotate(dance, int(move[1:]))
#     elif move[0] == "x":
#         index = list(map(int, move[1:].split("/")))
#         temp = dance[index[0]]
#         dance[index[0]] = dance[index[1]]
#         dance[index[1]] = temp
#     elif move[0] == "p":
#         index = list(move[1:].split("/"))
#         ind1 = dance.index(index[0])
#         ind2 = dance.index(index[1])
#         dance[ind1] = index[1]
#         dance[ind2] = index[0]

p = 0
        
while p < 1000000000:
    if dance in prevs:
        diff = len(prevs)-prevs.index(dance.copy())
        while p < 1000000000-diff:
            p += diff
    prevs.append(dance.copy())
    for move in data:
        if move[0] == "s":
            dance = rotate(dance, int(move[1:]))
        elif move[0] == "x":
            index = list(map(int, move[1:].split("/")))
            temp = dance[index[0]]
            dance[index[0]] = dance[index[1]]
            dance[index[1]] = temp
        elif move[0] == "p":
            index = list(move[1:].split("/"))
            ind1 = dance.index(index[0])
            ind2 = dance.index(index[1])
            dance[ind1] = index[1]
            dance[ind2] = index[0]
    p += 1
                     

ret = ""
for i in dance:
    ret += i
print(dance)
print(ret)
