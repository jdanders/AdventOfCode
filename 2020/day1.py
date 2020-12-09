nums = [int(ii) for ii in open('day1input.txt').readlines()]
f1 = True
f2 = True
for ii in range(len(nums)):
    for jj in range(len(nums)):
        if f1 and nums[ii] + nums[jj] == 2020:
            print(nums[ii] * nums[jj])
            f1 = False
        for kk in range(len(nums)):
            if f2 and nums[ii] + nums[jj] + nums[kk] == 2020:
                print(nums[ii] * nums[jj] * nums[kk])
                f2 = False
