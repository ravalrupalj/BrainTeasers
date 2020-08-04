#Check if an array is sorted and rotated

#Given a list of distinct integers, create a function that checks if the list is sorted and rotated clockwise. If so, return "YES"; otherwise return "NO".
def check(lst):
    posi = sorted(lst)
    for i in range(0,len(lst)-1):
        first=posi.pop(0)
        posi.append(first)
        if posi==lst:
            return "YES"

    return 'NO'

print(check([3, 4, 5, 1, 2]))
#➞ "YES"
# The above array is sorted and rotated.
# Sorted array: [1, 2, 3, 4, 5].
# Rotating this sorted array clockwise
# by 3 positions, we get: [3, 4, 5, 1, 2].

print(check([1, 2, 3]))
#➞ "NO"
# The above array is sorted but not rotated.

print(check([7, 9, 11, 12, 5]) )
#➞ "YES"
# The above array is sorted and rotated.
# Sorted array: [5, 7, 9, 11, 12].
# Rotating this sorted array clockwise
# by 4 positions, we get: [7, 9, 11, 12, 5].