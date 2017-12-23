import numpy as np

f = open("data21.txt")

start = """
.#.
..#
###"""

data = start.replace("\n", "")

#print(data)

data = np.array(list(data))

#print(data)

data = data.reshape((3,3))
# print(data)
# print()
# print(np.rot90(data))
# print()
# print(np.rot90(np.rot90(data)))
# print()
# print(np.rot90(np.rot90(np.rot90(data))))

inp = []
for line in f:
    line = line.strip("\n").split(" => ")
    inp.append((np.array(list(map(list, line[0].split("/")))),np.array(list(map(list, line[1].split("/"))))))

#print("here")
    
#print(np.array(inp[8][0]))

#[['.' '#' '#']
# ['#' '.' '#']
# ['.' '.' '#']]

def findMatch(pixels):
    found = False
    rots = 0
    flippedx = False
    flippedy = False
    while not found:
        for t, res in inp:
            #print("t", t[0], "pixels", pixels[0])
            if t.shape == pixels.shape and (pixels == t).all():
                found = True
                return res
        else:
            pixels = np.rot90(pixels)
            rots += 1
            #print("rotated")
            if rots >= 4 and not flippedx:
                rots = 0
                #print("flipping")
                pixels = np.fliplr(pixels)
            elif rots >= 4 and flippedx and not flippedy:
                pixels = np.fliplr(pixels)
                flippedx = False
                pixels = np.flipud(pixels)
                flippedy = True
                rots = 0
            if rots >= 4 and flippedx and flippedy:
                print("something wrong")
                break
    return ":("

for _ in range(18):
    size = len(data[0])
    if size % 2 == 0:
        times = size//2
    else:
        times = size//3
    htemp = np.hsplit(data, times)
    hstack = []
    for i in range(times):
        vtemp = np.vsplit(htemp[i], times)
        vstack = []
        for v in range(len(vtemp)):
            vstack.append(findMatch(np.array(vtemp[v])))
        if len(vstack) > 1:
            hstack.append(np.vstack(vstack))
        else:
            hstack = vstack
        # print(new)
        # print(new.shape)
        # print(list(new[2]))
        # test = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']])
        # print("test", test)
        # print((new == test).all())
    if len(hstack) > 1:
        data = np.hstack(hstack)
    else:
        data = hstack[0]
    print(data)


unique, counts = np.unique(data, return_counts=True)
print(dict(zip(unique, counts)))

