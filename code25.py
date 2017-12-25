

states = {
    "A": ((1,1,"B"),(0,1,"C")),
    "B": ((0,-1,"A"),(0,1,"D")),
    "C": ((1,1,"D"),(1,1,"A")),
    "D": ((1,-1,"E"),(0,-1,"D")),
    "E": ((1,1,"F"),(1,-1,"B")),
    "F": ((1,1,"A"),(1,1,"E"))
}

tape = [0 for _ in range(10000)]

head = len(tape)//2

state = "A"

## cycle?

for i in range(12368930):
    new = states[state][tape[head]]
    tape[head] = new[0]
    head += new[1]
    state = new[2]



print(tape.count(1))


