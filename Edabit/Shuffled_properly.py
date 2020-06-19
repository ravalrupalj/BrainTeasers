#Shuffled Properly?
#Given a list of 10 numbers, return whether or not the list is shuffled sufficiently enough. In this case, if 3 or more numbers appear consecutively (ascending or descending), return False.
def is_shuffled_well(lst):
    for i in range(8):
        diff = (lst[i] - lst[i+1], lst[i+1] - lst[i+2])
        if diff in ((-1, -1), (1, 1)):
            return False
    return True
print(is_shuffled_well([10, 1, 9, 4, 3, 2, 7, 8, 6, 5]))
#, False)
print(is_shuffled_well([5, 4, 3, 10, 9, 2, 7, 6, 8, 1]))
#, False)
print(is_shuffled_well([1, 10, 8, 9, 2, 3, 4, 7, 5, 6]))
#, False)
print((is_shuffled_well([1, 6, 4, 10, 3, 5, 7, 2, 9, 8])))
#True)
print(is_shuffled_well([10, 7, 9, 5, 4, 6, 3, 8, 2, 1]))
#True
print((is_shuffled_well([5, 6, 7, 9, 1, 10, 3, 8, 2, 4])))
# False
print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) )
#➞ False
# 1, 2, 3 appear consecutively
print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) )
#➞ False
# 9, 8, 7, 6 appear consecutively
print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) )
#➞ True
# No consecutive numbers appear
print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
#➞ True
# No consecutive numbers appear
#Notes
#Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
#You will get numbers from 1-10.