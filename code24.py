f = open("data24.txt")


ports = []
for line in f:
    ports.append(tuple(line.strip().split("/")))

ports2 = ports.copy()
    
startInd = ports.index(("0","30"))
start = ports[startInd]
print(start)

bridges = []
strengths = []

taken = [startInd]

def tuprev(tup):
    return (tup[1], tup[0])

def makeFirst(tup, first):
    if tup[0] == first:
        return tup
    return tuprev(tup)

def sumTouple(tup):
    return int(tup[0]) + int(tup[1])

def build(bridge, taken):
    ne = bridge[-1][-1]
    builtBridge = False
    for i in range(len(ports)):
        if i in taken:
            continue
        curr = ports[i]
        if ne in curr:
            build(bridge + [makeFirst(curr, ne)], taken + [i])
            builtBridge = True
    if not builtBridge:
        bridges.append(bridge.copy())
        strengths.append(sum(list(map(sumTouple, bridge))))
            

build([start], taken)



temp = strengths.copy()
temp.sort()
print(temp[-1])



def mapLen(l):
    return len(l)

temp = list(map(mapLen, bridges))
m = max(temp)
indices = [i for i, x in enumerate(temp) if x == m]

for i in indices:
    print(sum(list(map(sumTouple, bridges[i]))))


