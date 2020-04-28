#Check if Number is within a Given Range
#Given a number and a dictionary with min and max properties, return True if the number lies within the given range (inclusive).
#Examples
#is_in_range(4, { "min": 0, "max": 5 }) ➞ True
#is_in_range(4, { "min": 4, "max": 5 }) ➞ True
#is_in_range(4, { "min": 6, "max": 10 }) ➞ False
#is_in_range(5, { "min": 5, "max": 5 }) ➞ True
#Notes
#Numbers can be positive or negative, and they may not be integers.
#You can assume min <= max is always true.
#If you get stuck on a challenge, find help in the Resources tab.
#If you're really stuck, unlock solutions in the Solutions tab.
def is_in_range(n, r):
    return r['min']<=n<=r['max']

print(is_in_range(4, {"min": 0, "max": 5}))
print(is_in_range(4, {"min": 4, "max": 5}))
print(is_in_range(4, {"min": 6, "max": 10}))
print(is_in_range(5, {"min": 5, "max": 5}))