
f = open("data2.txt")


diffs = []

k = f.readline()

data = []

while k != "":
    k = ' '.join(k.split())
    data.append(list(map(int, k.strip("\n").split(" "))))
    diffs.append(max(data[-1])-min(data[-1]))
    k = f.readline()


print(sum(diffs))

divs = []

for row in data:
    breaking = False
    for first in range(len(row)):
        for second in range(len(row)):
            if first == second:
                continue
            if row[first] % row[second] == 0:
                divs.append(row[first]/row[second])
                breaking = True
                break
        if breaking:
            break

print(sum(divs))
            

