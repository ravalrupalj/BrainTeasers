#Find the Index (Part 1)
#Create a function that finds the index of a given item.

#search([1, 5, 3], 5) ➞ 1

#search([9, 8, 3], 3) ➞ 2

#search([1, 2, 3], 4) ➞ -1
#If the item is not present, return -1.


def search(lst, item):
    if item in lst:
        return lst.index(item)
    else:
        return -1


print(search([1, 5, 3], 5) )

print(search([9, 8, 3], 3) )

print(search([1, 2, 3], 4))