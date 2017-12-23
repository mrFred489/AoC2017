from collections import *

f = open("data20.txt")

data = []

def getData(inp):
    inp = inp.split("=")
    return inp[0], list(map(int, inp[1][1:-1].split(",")))
    

for line in f:
    temp = dict()
    line = line.strip().split(", ")
    for i in line:
        n, d = getData(i)
        temp[n] = d
    data.append(temp)

prevs = deque()

def updateData(inp):
    for i in range(3):
        inp["v"][i] += inp["a"][i]
        inp["p"][i] += inp["v"][i]
    return inp

def getDist(inp):
    return abs(inp[0]) + abs(inp[1]) + abs(inp[2]) 

datacpy = data.copy()

# for i in range(500):
#     minval = 99999
#     minInd = -1
#     for k in range(len(data)):
#         data[k] = updateData(data[k])
#         dist = getDist(data[k]["p"])
#         if dist < minval:
#             minval = dist
#             minInd = k
#     prevs.append(minInd)

# maxval = 99999
    
# while len(set(prevs)) != 1:
#     prevs.popleft()
#     minval = maxval
#     minInd = -1
#     for k in range(len(data)):
#         data[k] = updateData(data[k])
#         dist = getDist(data[k]["p"])
#         if dist < minval:
#             minval = dist
#             minInd = k
#         if dist > maxval:
#             maxval = dist
        
#     prevs.append(minInd)

    
# print(prevs)

cval = 500  #500

counter = cval



while counter != 0:
    toremove = []
    poss = []
    identify = dict()
    for k in range(len(data)):
        data[k] = updateData(data[k])
        if data[k]["p"] in poss:
            toremove.append(data[poss.index(data[k]["p"])])
            toremove.append(data[k])
        poss.append(data[k]["p"])
        
    if toremove == []:
        counter -= 1
    else:
        counter = cval
        for i in toremove:
            try:
                data.remove(i)
            except:
                pass
                
print(len(data))



