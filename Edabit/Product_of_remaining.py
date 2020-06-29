#Product of Remaining Elements
#Write a function that returns True if you can partition a list into one element and the rest, such that this element is equal to the product of all other elements excluding itself.
def can_partition(lst):

    l=[]
    for i in range(0,len(lst)):
        count = 1
        for j in range(0,len(lst)):
            if i!=j:
                count = count * lst[j]
            else:
                l.append(i)
        if count==lst[i]:
            return True
    return False
print(can_partition([2, 8, 4, 1]))
#➞ True
# 8 = 2 x 4 x 1
print(can_partition([-1, -10, 1, -2, 20]))
#➞ False
print(can_partition([-1, -20, 5, -1, -2, 2]))
#➞ True
#Notes
#The list may contain duplicates.
#Multiple solutions can exist, any solution is sufficient to return True.