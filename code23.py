from collections import defaultdict
import time

start = time.time()

f = open("data23.txt")

data = []

for i in f:
    data.append(i.strip().split())

pos = 0

regs = defaultdict(int)


prevPlay = -1

def valof(regs, val):
    if val.isdigit() or val[1:].isdigit():
        return int(val)
    return regs[val]

statuss = ["ok", "ok"]
c = 0
while 0 <= pos < len(data):
    curr = data[pos]
    #print(pos,regs["h"], regs["g"])
    if curr[0] == "set":
        regs[curr[1]] = valof(regs, curr[2])
    elif curr[0] == "mul":
        c += 1
        regs[curr[1]] *= valof(regs, curr[2])
    elif curr[0] == "sub":
        regs[curr[1]] -= valof(regs, curr[2])
    elif curr[0] == "jnz":
        if valof(regs, curr[1]) != 0:
            pos += valof(regs, curr[2])
            continue
    pos += 1


print(c)


# del2

regs = defaultdict(int)

regs["a"] = 1

regs["b"] = 106500
regs["c"] = 123500

c = 0

while True:
    regs["f"] = 1
    regs["d"] = 2
    while regs["g"] != 0:
        if regs["b"] % regs["d"] == 0:
            regs["f"] = 0
        regs["d"] += 1
        regs["g"] = regs["d"] - regs["b"]
    if regs["f"] == 0:
        regs["h"] += 1
    regs["g"] = regs["b"] - regs["c"]
    if regs["g"] == 0:
        break
    regs["b"] += 17

    




print(regs["h"])
print(time.time()-start)    
