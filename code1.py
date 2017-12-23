
f = open("data1.txt")

data = f.readline()

data = data.strip()

num = 0
for i in range(1,len(data)):
    if data[i-1] == data[i]:
        num += int(data[i])

if data[0] == data[-1]:
    num += int(data[0])

print("svar1")
print(num)

k = int(len(data)/2)
num2 = 0
for i in range(len(data)):
    if k + i < len(data):
        ind2 = k+i
    else:
        ind2 = k+i-len(data)
    if data[i] == data[ind2]:
        num2 += int(data[i])

print(num2)        

num3 = 0

for i in range(len(data)):
    if data[i] == data[(i+k)%len(data)]:
        num3 += int(data[i])
print(num3)
