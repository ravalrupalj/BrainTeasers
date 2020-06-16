#1365. How Many Numbers Are Smaller Than the Current Number

def smallerNumbersThanCurrent(nums):
    count = 0
    l = []
    for i in range(0, len(nums)):
        number = nums[i]

        for t in range(0, len(nums)):
            if number > nums[t]:
                count = count + 1
        l.append(count)
        count = 0
    return l

print(smallerNumbersThanCurrent([8,1,2,2,3]))