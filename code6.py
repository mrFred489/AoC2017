f = open("data6.txt")


data = list(map(int, f.readline().strip("\n").split("\t")))
datacopy = data.copy()

previuss = []
previuss.append(data.copy())

steps = 0

while True:
    steps += 1
    maxm = data.index(max(data))
    distribute = data[maxm]
    data[maxm] = 0
    for i in range(distribute):
        ind = (maxm + i + 1) % len(data)
        data[ind] += 1
    if data.copy() in previuss:
        print(steps)
        print(len(previuss)-previuss.index(data.copy()))
        break

    previuss.append(data.copy())




