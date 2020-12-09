lines = [ii.strip() for ii in open('day4input.txt').readlines()]
pp = []
current_pp = {}
# Build up passport list
for line in lines:
    if not line:
        # blank line means new passport
        pp.append(current_pp)
        current_pp = {}
    else:
        # otherwise add each entry on the line
        for kpair in line.split():
            current_pp[kpair.split(":")[0]] = kpair.split(":")[1]

# Add final passport if didn't end in blank line
if current_pp:
    pp.append(current_pp)

# Define validating functions for each field
def year_valid(val, least, most):
    if int(val) >= least and int(val) <= most:
        return True
    return False

def byr_valid(val):
    return year_valid(val, 1920, 2002)

def iyr_valid(val):
    return year_valid(val, 2010, 2020)

def eyr_valid(val):
    return year_valid(val, 2020, 2030)

def hgt_valid(val):
    if "cm" in val:
        hgt = int(val.replace("cm", ""))
        if hgt >= 150 and hgt <= 193:
            return True
    if "in" in val:
        hgt = int(val.replace("in", ""))
        if hgt >= 59 and hgt <= 76:
            return True
    return False

def hcl_valid(val):
    if val[0] != "#":
        return False
    if len(val) != 7:
        return False
    try:
        color = int(val[1:], 16)
        return True
    except:
        pass
    return False

def ecl_valid(val):
    if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False

def pid_valid(val):
    if len(val) != 9:
        return False
    try:
        pid = int(val)
        return True
    except:
        pass
    return False

def cid_valid(val):
    return True

fields = [
    ("byr", byr_valid),
    ("iyr", iyr_valid),
    ("eyr", eyr_valid),
    ("hgt", hgt_valid),
    ("hcl", hcl_valid),
    ("ecl", ecl_valid),
    ("pid", pid_valid),
    ("cid", cid_valid),
]

good = 0

# part 1
for cpp in pp:
    bad = False
    for field, validator in fields:
        if field not in cpp and field != "cid":
            bad = True
    if not bad:
        good += 1

print(good)


# part 2
good = 0
for cpp in pp:
    bad = False
    for field, validator in fields:
        if field not in cpp and field != "cid":
            bad = True
        if field in cpp and not validator(cpp[field]):
            bad = True
    if not bad:
        good += 1

print(good)
