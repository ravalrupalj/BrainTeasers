#Write a function that moves all elements of one type to the end of the list.
#Keep the order of the un-moved items the same.
def move_to_end(lst,l):

    for i in lst:
        if i==l:
            lst.remove(i)
            lst.append(i)
    return lst
print(move_to_end([1, 3, 2, 4, 4, 1], 1))
#➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
#➞ [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a"))
#➞ ["b", "a", "a", "a"]

