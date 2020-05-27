#Strictly Increasing or Decreasing
#Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.
#The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
#Input lists have a minimum length of 2.
def check(lst):
    if all(x < y for x, y in zip(lst, lst[1:])):
        return 'increasing'
    elif all(x > y for x, y in zip(lst, lst[1:])):
        return 'decreasing'
    else:
        return 'neither'
print(check([1, 2, 3]) )
#➞ "increasing"
print(check([3, 2, 1]) )
#➞ "decreasing"
print(check([1, 2, 1]))
#➞ "neither"
print(check([1, 1, 2]))
#➞ "neither"

