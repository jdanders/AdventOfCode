lines = [ii.strip() for ii in open('day6input.txt').readlines()]

group = 0
total = 0
answers = []
for line in lines:
    answers += [i for i in line]
    if not line:
        s = set(answers)
        total += len(s)
        answers = []


# Tail
s = set(answers)
total += len(s)
print(total)


group = 0
total = 0
answers = []
for line in lines:
    if line:
        answers += [line]
    else:
        s = set(answers[0])
        for aa in answers[1:]:
            s = s & set(aa)
        total += len(s)
        answers = []

s = set(answers[0])
for aa in answers[1:]:
    s = s & set(aa)
total += len(s)
print(total)
