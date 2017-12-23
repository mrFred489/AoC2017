from collections import deque
f = 376

data = [0,1]

index = 1

for i in range(2,2018):
    index += f
    index %= len(data)
    index += 1
    data.insert(index, i)
    if i % 10000 == 0:
        print(i)


print(data[index-5:index+5])

data = deque([0, 1])

index = 1

prevInd = 1
print(list(range(10)))
for i in range(2,50000000):
    index += f
    index %= len(data)
    data.rotate(prevInd - index)
    #print("indexes", prevInd, index)
    #print("rotate", prevInd - index)
    data.append(i)
    if i % 1000000 == 0:
        print(i)
    prevInd = index
    #print(data)

data.rotate(-10)
    
temp = list(data)

ind = temp.index(0)
ind2 = temp.index(2017)

print(temp[ind2-5:ind2+5])
print(temp[ind-5:ind+5])

