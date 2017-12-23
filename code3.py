import math


data = 347991

def del1():
    m = [[0]*2000 for _ in range(2000)]
    
    direction = 0
    
    startx = 1000
    starty = 1000
    
    x = 1001
    y = 1000
    
    m[y][1000] = 1
    m[y][1001] = 2
    
    for i in range(3, data+1):
        if direction == 0:
            if m[y-1][x] == 0:
                y -= 1
                direction = 1
            else:
                x += 1
        elif direction == 1:
            if m[y][x-1] == 0:
                x -= 1
                direction = 2
            else:
                y -= 1
        elif direction == 2:
            if m[y+1][x] == 0:
                y += 1
                direction = 3
            else:
                x -= 1
        elif direction == 3:
            if m[y][x+1] == 0:
                x += 1
                direction = 0
            else:
                y += 1 
        m[y][x] = i
    
    print("x er: {}".format(x))
    print("y er: {}".format(y))
    
    print(abs(startx - x) + abs(starty - y))


def del2():
    m2 = [[0]*2000 for _ in range(2000)]
    direction = 0
    x = 1001
    y = 1000
    m2[y][1000] = 1
    m2[y][1001] = 1
    
    
    def sumArea(m, x, y):
        ret = 0
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                ret += m[y+j][x+k]
        ret = m[y-1][x-1] + m[y-1][x] + m[y-1][x+1] + m[y][x-1] + m[y][x+1] + m[y+1][x-1] + m[y+1][x] + m[y+1][x+1]
        return ret
        
    
    
    for i in range(3, data+1): # data+1
        if direction == 0:
            if m2[y-1][x] == 0:
                y -= 1
                direction = 1
            else:
                x += 1
        elif direction == 1:
            if m2[y][x-1] == 0:
                x -= 1
                direction = 2
            else:
                y -= 1
        elif direction == 2:
            if m2[y+1][x] == 0:
                y += 1
                direction = 3
            else:
                x -= 1
        elif direction == 3:
            if m2[y][x+1] == 0:
                x += 1
                direction = 0
            else:
                y += 1 
        m2[y][x] = sumArea(m2, x, y)
    
        if m2[y][x] > data:
            break
    print(m2[y][x])
    print("x er: {}".format(x))
    print("y er: {}".format(y))

    for i in range(-10,10):
        print(m2[1000+i][990:1010])
    

del1()
del2()
        
