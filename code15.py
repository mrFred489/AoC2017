

numA = 116
numB = 299

Afactor = 16807
Bfactor = 48271

divFactor = 2147483647

def genNum(prevA, prevB):
    return (Afactor * prevA) % divFactor,(Bfactor * prevB) % divFactor


# lst = []


# for i in range(40000000):
#     numA, numB = genNum(numA, numB)
#     lst.append(len(set([format(numA, '016b')[-16:], format(numB, '016b')[-16:]])))

# print(lst.count(1))

def genNumA(prevA):
    num = (Afactor * prevA) % divFactor
    while num % 4 != 0:
        num = (Afactor * num) % divFactor
    return num

def genNumB(prevB):
    num = (Bfactor * prevB) % divFactor
    while num % 8 != 0:
        num = (Bfactor * num) % divFactor
    return num

def gen(num, fac, mod):
    while True:
        num *= fac
        num %= divFactor
        if num % mod == 0:
            yield num
        
        
numA = 116
numB = 299

GA = gen(116, Afactor, 4)
GB = gen(299, Bfactor, 8)

lst = []

for i in range(5000000):
    numA = next(GA)
    numB = next(GB)
    lst.append(len(set([format(numA, '016b')[-16:], format(numB, '016b')[-16:]])))
    if i % 500000 == 0:
        print(i)
    
print(lst.count(1))


