#Fix the Error: Mutating Arrays
#Suppose I want to define a function that removes the last element of a list each time I call it, but does not mutate the original list. Fix the code so that the results are no longer mutating the list.
x = [1, 2, 3, 4, 5]
#minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
#minus_one(x) ➞ [1, 2, 3]  # 2nd time function is called.
#minus_one(x) ➞ [1, 2]  # 3rd time function is called.
#minus_one(x) ➞ [1]  # 4th time function is called.
# What I want instead:
#minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
#minus_one(x) ➞ [1, 2, 3, 4]  # 2nd time function is called.
#minus_one(x) ➞ [1, 2, 3, 4]  # 3rd time function is called.
#minus_one(x) ➞ [1, 2, 3, 4]  # 4th time function is called.
def minus_one(lst):
    t=lst.copy()
    t.pop(-1)
    return t
print(minus_one(x))
print(minus_one(x))
print(minus_one(x))