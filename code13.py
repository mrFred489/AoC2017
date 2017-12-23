f = open("data13.txt")


severity = 0


data = []

for line in f:
    line = list(map(int, line.strip().split(": ")))
    data.append(line)
    severity += int((line[0]) % (line[1]*2-2) == 0) * line[0] * line[1]
    if (line[0] % (line[1]*2-2) == 0):
        print(line[0], line[1])

def isSafe(data, delay):
    for line in data:
        if (line[0]+delay) % (line[1]*2-2) == 0:
            return False
    return True
print(severity)
        
result = False

delay = 10


while not result:
    result = isSafe(data, delay)
    delay += 1
    
print(delay-1)        

