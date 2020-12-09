lines = [ii.strip() for ii in open('day3input.txt').readlines()]
xmod = len(lines[0])
x = 3
y = 1
trees = 0
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
result = 1
for xplus, yplus in slopes:
    x = xplus
    y = yplus
    trees = 0
    while y < len(lines):
        if lines[y][x % xmod] == '#':
            trees += 1
        x += xplus
        y += yplus
    print(trees)
    result *= trees

print("Results", result)
