lines = [int(ii.strip()) for ii in open('day9input.txt').readlines()]
preamble = lines[:25]
for num in lines[25:]:
    result = False
    for numa in preamble:
        for numb in preamble:
            if numa + numb == num:
                result = True
                break
        if result:
            break
    if not result:
        break
    preamble = preamble[1:] + [num]

print(num)

for start_point in range(len(lines)):
    end_point = start_point + 2
    while sum(lines[start_point:end_point]) < num:
        end_point += 1
    if sum(lines[start_point:end_point]) == num:
        print("Found range")
        print("min", min(lines[start_point:end_point]))
        print("max", max(lines[start_point:end_point]))
        print("Sum", min(lines[start_point:end_point]) + max(lines[start_point:end_point]))
