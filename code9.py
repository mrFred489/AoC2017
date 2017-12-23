f = open("data9.txt")



data = f.readline()

depth = 0

totalScore = 0

skipping = False

garbage = False

garbageCounter = 0

for c in data:
    if skipping:
        skipping = False
        continue
    if garbage:
        if c == ">":
            garbage = False
            continue
        elif c == "!":
            skipping = True
            continue
        garbageCounter += 1
    else:
        if c == "{":
            depth += 1
        elif c == "}":
            totalScore += depth
            depth -= 1
        elif c == "<":
            garbage = True


print(totalScore)
print(garbageCounter)
            
            


