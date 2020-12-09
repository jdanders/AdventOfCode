lines = [ii.strip() for ii in open('day8input.txt').readlines()]

visited = [False]*len(lines)
accum = 0
ptr=0
while True:
    if visited[ptr]:
        break
    cmd = lines[ptr]
    next_ptr = ptr + 1
    value = int(cmd.split()[1])
    if (cmd.startswith("acc")):
        accum += value
    if (cmd.startswith("jmp")):
        next_ptr = ptr + value
    visited[ptr] = True
    ptr = next_ptr

print("First", accum)

changed = 0
while changed < len(lines):
    newlines = [line for line in lines]
    while lines[changed].startswith('acc'):
        changed += 1
    if lines[changed] == "nop":
        newlines[changed] = newlines[changed].replace("nop","jmp")
    else:
        newlines[changed] = newlines[changed].replace("jmp","nop")
    visited = [False]*len(lines)
    accum = 0
    ptr=0
    while True:
        if visited[ptr]:
            break
        cmd = newlines[ptr]
        next_ptr = ptr + 1
        value = int(cmd.split()[1])
        if (cmd.startswith("acc")):
            accum += value
        if (cmd.startswith("jmp")):
            next_ptr = ptr + value
        visited[ptr] = True
        ptr = next_ptr
        if ptr == len(lines):
            print("Done", accum)
            break
    changed += 1
