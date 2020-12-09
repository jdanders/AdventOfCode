lines = [ii.strip() for ii in open('day5input.txt').readlines()]

def get_num(directions, size):
    left = 0
    right = size
    for letter in directions:
        size = right - left + 1
        # Lower half
        if letter == 'F' or letter == 'L':
            right -= size/2
        # Upper half
        else:
            left += size/2
        print(left, right)
    if left != right:
        print("FAILED", directions, size)
    return left

max_seat = 0
found_seats = [False]*128*8
for line in lines:
    row, column = (get_num(line[:7], 127), get_num(line[7:], 7))
    seatid = row * 8 + column
    if seatid > max_seat:
        max_seat = seatid
    if found_seats[seatid]:
        print("ERROR")
    found_seats[seatid] = True

print(max_seat)

for ii in range(len(found_seats)):
  if ii > 1 and ii < 1023:
    if not found_seats[ii] and found_seats[ii-1] and found_seats[ii+1]:
        print("You are %d"%ii)
