#All Occurrences of an Element in a List
#Create a function that returns the indices of all occurrences of an item in the list.
#Notes
#If an element does not exist in a list, return [].
#Lists are zero-indexed.
#Values in the list will be value-types (don't need to worry about nested lists).
def get_indices(lst,el):
    l=[]
    for i,j in enumerate(lst):
        if j==el:
            l.append(i)
    return l
print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
#➞ [0, 1, 3, 5]
print(get_indices([1, 5, 5, 2, 7], 7) )
#➞ [4]
print(get_indices([1, 5, 5, 2, 7], 5) )
#➞ [1, 2]
print(get_indices([1, 5, 5, 2, 7], 8) )
#➞ []
