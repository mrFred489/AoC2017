import time

f = open("data5.txt")

data = []

for line in f:
    data.append(int(line.strip()))

data2 = data.copy()
    
index = 0
steps = 0
start = time.time()    
try:
    while True:
        data[index] += 1
        index += data[index]-1
        steps += 1
except IndexError as e:
    print(steps)
print("Tid for del 1: {}".format(time.time()-start))
    
index = 0
steps = 0
start = time.time()    
try:
    while True:
        if data2[index] >= 3:
            data2[index] -= 1
            index += data2[index]+1
        else:
            data2[index] += 1
            index += data2[index]-1
        steps += 1
except IndexError as e:
    print(steps)

    
print("Tid for del 2: {}".format(time.time()-start))
