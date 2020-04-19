#Fix The Bug: Simple List Manipulation
#Help fix all the bugs in the function increment_items! It is intended to add 1 to every element in the list!
##Examples
# #increment_items([0, 1, 2, 3]) ➞ [1, 2, 3, 4]
#increment_items([2, 4, 6, 8]) ➞ [3, 5, 7, 9]
#increment_items([-1, -2, -3, -4]) ➞ [0, -1, -2, -3]
def increment_items(lst):
	return [i+1 for i in lst]



print(increment_items([0, 1, 2, 3]))
print(increment_items([2, 4, 6, 8]))
print(increment_items([-1, -2, -3, -4]))