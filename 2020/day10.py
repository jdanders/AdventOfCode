lines = [int(ii.strip()) for ii in open('day10input.txt').readlines()]

lines.sort()
lines = [0] + lines + [lines[-1] + 3]
diff = [1]*4

for ii in range(len(lines)-1):
    diff[lines[ii+1] - lines[ii]] += 1

print(f"Part 1: {diff[1] * diff[3]}")


# Straight up recursion
def lame_num_paths(index, history):
    total = 0
    num = lines[index]
    nhist = [ii for ii in history]
    nhist.append(num)
    if (index == len(lines) - 1):
        # print("** ", nhist)
        return 1
    if (index+1 < len(lines) and lines[index+1] - num <= 3):
        total += lame_num_paths(index+1, nhist)
        if (index+2 < len(lines) and lines[index+2] - num <= 3):
            total += lame_num_paths(index+2, nhist)
            if (index+3 < len(lines) and lines[index+3] - num <= 3):
                total += lame_num_paths(index+3, nhist)
    # print(total)
    return total


# Strategy: count the numbers of forks for each position, and multiply that
# by the number of ways to hit that position
def num_paths():
    hits = [0]*len(lines)
    # Start with 1 path, the path with no jumps
    total = 1
    hits[0] = 1
    for ii, num in enumerate(lines[:-1]):
        newpaths = 0
        # Will definitely hit pos 1, the next option
        hits[ii+1] += hits[ii]
        # Check if new paths are possible by jumping to pos 2 or 3 from here
        for jump_ii, jump_num in enumerate(lines[ii+2:ii+4]):
            if jump_num - num <= 3:
                # This position jumps, so record extra hits and paths
                hits[jump_ii + ii + 2] += hits[ii]
                newpaths += 1
                # print(f"added {num} to {lines[jump_ii]}")
        total += newpaths * hits[ii]
        # print(f"{ii}: {newpaths} h{hits[ii]} sum {total}")
    return total


print(f"Part 2: {num_paths()}")
