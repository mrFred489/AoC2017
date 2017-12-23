f = open("data7.txt")


children = dict()


weights = dict()
allNames = set()
allChildren = set()

counter = 0


for line in f:
    temp = list(line.strip("\n").replace(",", "").split())
    name = temp[0]
    weight = int(temp[1][1:-1])
    weights[name] = weight
    kids = temp[3:]
    allNames.add(name)
    children[name] = kids
    for kid in kids:
        allChildren.add(kid)
    counter += 1

parent = (allNames-allChildren).pop()
    
print("part1", parent)


def traverse(name, fix=0):
    res = weights[name]
    wchilds = set()
    kidsweight = 0
    for i in children[name]:
        kid, b = traverse(i)
        if not b:
            return 0, False
        res += kid
        kidsweight += kid
        wchilds.add(kid)
    if fix > 0:
        maybe = fix-kidsweight
        if weights[name] != maybe:
            print("part2", maybe)
        return 0, False
    if len(wchilds) > 1:
        for i in children[name]:
            traverse(i, list(wchilds)[1])
    return res, len(wchilds) <= 1


traverse(parent)

