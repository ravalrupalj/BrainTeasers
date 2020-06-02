#Is One List a Subset of Another?
#Create a function that returns True if the first list is a subset of the second. Both lists will contain only unique values.
def is_subset(a,b):
    for i in a:
        if i not in b:
            return False
    return True


print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]) )
#➞ True
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]) )
#➞ True

print(is_subset([1, 2], [3, 5, 9, 1]) )
#➞ False

