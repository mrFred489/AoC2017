import functools

maxnum = 256

#p2_lengths = list(map(ord, "")) + extra

def circ_slice(a, start, length):
    return (a * 2)[start:start+length]

def circ_insert(a, start, length, ins):
    temp = (a * 2)
    temp[start:start+length] = ins
    return temp[len(a):len(a)+start] + temp[start:len(a)]

def p1(lengths, index, data, skip_size):
    for length in lengths:
        temp = circ_slice(data, index, length)
        temp.reverse()
        data = circ_insert(data, index, length, temp)
        index += (length + skip_size)
        index = index % maxnum
        skip_size += 1
    return index, data, skip_size

def knothash(input):
    extra = [17, 31, 73, 47, 23]
    p2_lengths = list(map(ord, input.strip())) + extra
    maxnum = 256

    data = [i for i in range(maxnum)]

    index0 = 0
    
    skip_size = 0
    
    index = 0
    
    for i in range(64):
        index, data, skip_size = p1(p2_lengths, index, data, skip_size)
    
        
    dense = [functools.reduce(lambda a,b: a ^ b, data[i*16:i*16+16], 0) for i in range(0,16)]
    
    ret = ""
    
    for i in dense:
        ret += format(i, '02x')
    return ret

count = 0

data = []

for i in range(128):
    res = knothash("ljoxqyyw-" + str(i))
    res2 = ""
    for i in res:
        res2 += "{0:04b}".format(int(i, 16))
    count += res2.count("1")
    data.append(list(res2))

print(count)

def checkRegion(x, y, data, name):
    if (x-1) >= 0 and data[x-1][y] == "1":
        data[x-1][y] = name
        data = checkRegion(x-1, y, data.copy(), name)
    if x < 127 and data[x+1][y] == "1":
        data[x+1][y] = name
        data = checkRegion(x+1, y, data.copy(), name)
    if (y-1) >= 0 and data[x][y-1] == "1":
        data[x][y-1] = name
        data = checkRegion(x, y-1, data.copy(), name)
    if y < 127 and data[x][y+1] == "1":
        data[x][y+1] = name
        data = checkRegion(x, y+1, data.copy(), name)
    return data

regions = 0

for x in range(128):
    for y in range(128):
        if data[x][y] == "1":
            regions += 1
            data[x][y] = str(regions+1)
            data = checkRegion(x, y, data.copy(), str(regions+1))

# for i in data:
#     print(i[:30])
            
print(regions)
