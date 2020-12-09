from dataclasses import dataclass
lines = [ii.strip() for ii in open('day7input.txt').readlines()]
target = 'shiny gold'
rules = {}


@dataclass
class Rule:
    color: str
    qty: int


# Build the rule dictionary. index: color, contents: list of Rule classes
for line in lines:
    # Break line into outer bag and allowed inner bags
    outer = line.split(" bags")[0]
    inners = line.split("contain ")[1].split(", ")
    if "no other bags" in inners[0]:
        rules[outer] = []
        continue
    inner_list = []
    for inner in inners:
        inner = inner.split(" bag")[0]
        (qty, color) = inner.split(" ", 1)
        inner_list.append(Rule(color, int(qty)))
    rules[outer] = inner_list


# Part 1
def color_in_bag(color, bag):
    result = False
    for inner in rules[bag]:
        if inner.color == color:
            return True
        result |= color_in_bag(color, inner.color)
    return result


matches = 0
for bag in rules.keys():
    matches += color_in_bag(target, bag)

print(matches)


# Part 2
def count_subbags(color):
    # Start by counting this bag
    result = 1
    # Add in sub-bags
    for inner in rules[color]:
        result += count_subbags(inner.color) * inner.qty
    return result


print(count_subbags(target) - 1)
