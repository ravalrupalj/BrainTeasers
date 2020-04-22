#Same Number of Unique Elements
#Write a function that returns True if two lists have the same number of unique elements, and False otherwise.
#lst1 = [1, 3, 4, 4, 4]
#lst2 = [2, 5, 7]
#In lst1, the number 4 appears three times, which means it contains three unique elements: [1, 3, 4]. Since lst1 and lst2 both contain the same number of unique elements, this example would return True.
#same([1, 3, 4, 4, 4], [2, 5, 7]) ➞ True
#same([9, 8, 7, 6], [4, 4, 3, 1]) ➞ False
#same([2], [3, 3, 3, 3, 3]) ➞ True
def same(a1, a2):
    return len(set(a1))==len(set(a2))

print(same([1, 3, 4, 4, 4], [2, 5, 7]))
print(same([9, 8, 7, 6], [4, 4, 3, 1]) )
print(same([2], [3, 3, 3, 3, 3]) )
