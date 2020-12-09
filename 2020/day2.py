rules = [ii for ii in open('day2input.txt').readlines()]
good = 0
bad = 0
for rule in rules:
  if '-' in rule:
    rng, letter, pw = rule.split()
    least = int(rng.split('-')[0])
    most = int(rng.split('-')[1])
    num = pw.count(letter[0])
    if num >= least and num <= most:
        good += 1
    else:
        bad += 1

print("1: good", good)
print("1: bads", bad)

good = 0
bad = 0
for rule in rules:
  if '-' in rule:
    rng, letter, pw = rule.split()
    least = int(rng.split('-')[0])
    most = int(rng.split('-')[1])
    num = (pw[least-1] == letter[0]) + (pw[most-1] == letter[0])
    if num == 1:
        good += 1
    else:
        bad += 1
        print(rule)

print("2: good", good)
print("2: bads", bad)
