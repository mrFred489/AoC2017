import functools

f = open("data12.txt")


data = dict()

visited = set()

for line in f:
    temp = line.strip("\n").split(" <-> ")
    data[temp[0]] = temp[1].split(", ")

def visit(name, visited):
    children = set()
    for child in data[name]:
        if child not in visited:
            visited.add(child)
            visited = visited.union(visit(child, visited))
    return visited

print(len(visit("0", set())))

groups = []

for key in data.keys():
    if groups == [] or key not in functools.reduce(set.union, groups):
        groups.append(visit(key, set()))

print(len(groups))

