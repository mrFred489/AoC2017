f = open("data4.txt")

counter = 0

phrases = []

for line in f:
    data = line.strip("\n").split(" ")
    counter += int(len(data) == len(set(data)))
    phrases.append(data)
print(counter)

def k(x):
    return ''.join(sorted(x))



counter2 = 0
for line in phrases:
    temp = list(map(k, line))
    counter2 += (len(line) == len(set(temp)))

print(counter2)
    
