from collections import defaultdict
import time

f = open("data18.txt")

data = []

for i in f:
    data.append(i.strip().split())

pos = 0

regs = defaultdict(int)

prevPlay = -1

def valof(regs, val):
    if val.isdigit() or val[1:].isdigit():
        return int(val)
    return regs[val]

statuss = ["ok", "ok"]

while 0 <= pos < len(data):
    addpos = True
    curr = data[pos]
    print(curr)
    if curr[0] == "snd":
        prevPlay = valof(regs, curr[1])
    elif curr[0] == "set":
        regs[curr[1]] = valof(regs, curr[2])
    elif curr[0] == "add":
        regs[curr[1]] += valof(regs, curr[2])
        print("added", regs[curr[1]])
    elif curr[0] == "mul":
        regs[curr[1]] *= valof(regs, curr[2])
    elif curr[0] == "mod" and valof(regs, curr[2]) != 0:
        regs[curr[1]] %= valof(regs, curr[2])
    elif curr[0] == "rcv":
        if valof(regs, curr[1]) > 0:
            print(prevPlay)
            break
    elif curr[0] == "jgz":
        if valof(regs, curr[1]) > 0:
            pos += valof(regs, curr[2])
            addpos = False
    if addpos:
        pos += 1

# while 0 <= pos < len(data):
#     addpos = True
#     curr = data[pos]
#     print(curr)
#     if curr[0] == "snd":
#         otherqueue.put(valof(regs, curr[1]))
#     elif curr[0] == "set":
#         regs[curr[1]] = valof(regs, curr[2])
#     elif curr[0] == "add":
#         regs[curr[1]] += valof(regs, curr[2])
#         print("added", regs[curr[1]])
#     elif curr[0] == "mul":
#         regs[curr[1]] *= valof(regs, curr[2])
#     elif curr[0] == "mod" and valof(regs, curr[2]) != 0:
#         regs[curr[1]] %= valof(regs, curr[2])
#     elif curr[0] == "rcv":
#         if valof(regs, curr[1]) > 0:
#             statuss[regs["p"]] = "waiting"
#             regs[curr[1]] = myqueue.get()
#             statuss[regs["p"]] = "ok"
#     elif curr[0] == "jgz":
#         if valof(regs, curr[1]) > 0:
#             pos += valof(regs, curr[2])
#             addpos = False
#     if addpos:
#         pos += 1

print(regs)
    
print(prevPlay)

import _thread
import queue


snds = queue.Queue()

def work(myid, regs, myqueue, otherqueue):
    global snds
    pos = 0
    while 0 <= pos < len(data):
        addpos = True
        curr = data[pos]
        if curr[0] == "snd":
            otherqueue.put(valof(regs, curr[1]))
            print(myid, "sending", curr, pos)
            if myid == 1:
                snds.put(1)
        elif curr[0] == "set":
            regs[curr[1]] = valof(regs, curr[2])
        elif curr[0] == "add":
            regs[curr[1]] += valof(regs, curr[2])
        elif curr[0] == "mul":
            regs[curr[1]] *= valof(regs, curr[2])
        elif curr[0] == "mod" and valof(regs, curr[2]) != 0:
            regs[curr[1]] %= valof(regs, curr[2])
        elif curr[0] == "rcv":
            statuss[myid] = "waiting"
            regs[curr[1]] = myqueue.get()
            statuss[myid] = "ok"
        elif curr[0] == "jgz":
            if valof(regs, curr[1]) > 0:
                pos += valof(regs, curr[2])
                addpos = False
        if addpos:
            pos += 1
    statuss[regs["p"]] = "waiting"
q0_regs = defaultdict(int)
q0_regs["p"] = 0

q1_regs = defaultdict(int)
q1_regs["p"] = 1

q0 = queue.Queue()
q1 = queue.Queue()

_thread.start_new_thread(work , (0, q0_regs, q0, q1) )
_thread.start_new_thread(work , (1, q1_regs, q1, q0) )
breaking = False
abouttobreak = 0
while not breaking:
    if statuss[0] == "waiting" and statuss[1] == "waiting":
        abouttobreak += 1
    else:
        abouttobreak = 0
    if abouttobreak > 1:
        breaking = True
    time.sleep(0.1)
        


print(snds.qsize())
