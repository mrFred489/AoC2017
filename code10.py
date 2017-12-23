import functools

f = open("data10.txt")
# f = open("data10test.txt")

extra = [17, 31, 73, 47, 23]
file0 = f.readline().strip("\n").strip(" ")
maxnum = 256

p1_lengths = list(map(int, file0.split(",")))
p2_lengths = list(map(ord, file0.strip())) + extra
#p2_lengths = list(map(ord, "")) + extra


def circ_slice(a, start, length):
    return (a * 2)[start:start+length]

def circ_insert(a, start, length, ins):
    temp = (a * 2)
    temp[start:start+length] = ins
    return temp[len(a):len(a)+start] + temp[start:len(a)]

data = [i for i in range(maxnum)]

index0 = 0

skip_size = 0

index = 0

def p1(lengths, index, data, skip_size):
    for length in lengths:
        temp = circ_slice(data, index, length)
        temp.reverse()
        data = circ_insert(data, index, length, temp)
        index += (length + skip_size)
        index = index % maxnum
        skip_size += 1
    return index, data, skip_size

i, data1, s = p1(p1_lengths, index, data.copy(), skip_size)

print("part1:", data1[0]*data1[1])

for i in range(64):
    index, data, skip_size = p1(p2_lengths, index, data, skip_size)

    
dense = [functools.reduce(lambda a,b: a ^ b, data[i*16:i*16+16], 0) for i in range(0,16)]

ret = ""

for i in dense:
    ret += format(i, '02x')

print("part2:", ret)
print(len(ret))
    



