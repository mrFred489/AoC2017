f = open("data8.txt")

data = dict()

counter = 0

def doCond(data, condl, cond, condr):
    if cond == "<":
        return data[condl] < condr
    elif cond == ">":
        return data[condl] > condr
    elif cond == "!=":
        return data[condl] != condr
    elif cond == "<=":
        return data[condl] <= condr
    elif cond == ">=":
        return data[condl] >= condr
    elif cond == "==":
        return data[condl] == condr

def doChange(data, change, num, reg):
    if change == "inc":
        data[reg] += num
    else:
        data[reg] -= num
    return data

maxv = 0
for line in f:
    n, change, num, _, condl, cond, condr = line.strip("\n").split(" ")
    num = int(num)
    condr = int(condr)
    if n not in data.keys():
        data[n] = 0
    if condl not in data.keys():
        data[condl] = 0

    if doCond(data, condl, cond, condr):
        data = doChange(data, change, num, n)
    t = max(data.values())
    if t > maxv:
        maxv = t

print(max(data.values()))
print(maxv)
