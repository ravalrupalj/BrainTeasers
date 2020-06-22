#Reorder Digits
#Create a function that reorders the digits of each numerical element in a list based on ascending (asc) or descending (desc) order.
def reorder_digits(lst, direction):
    final_l=[]
    for i in lst:
        t=''.join(sorted(str(i)))
        if direction=='asc':
            final_l.append(int(t))
        else:
            final_l.append(int(t[::-1]))
    return final_l



print(reorder_digits([515, 341, 98, 44, 211], "asc"))
#➞ [155, 134, 89, 44, 112]
print(reorder_digits([515, 341, 98, 44, 211], "desc"))
#➞ [551, 431, 98, 44, 211]
print(reorder_digits([63251, 78221], "asc"))
#➞ [12356, 12278]
print(reorder_digits([63251, 78221], "desc"))
#➞ [65321, 87221]
print(reorder_digits([1, 2, 3, 4], "asc"))
#➞ [1, 2, 3, 4]
print(reorder_digits([1, 2, 3, 4], "desc"))
#➞ [1, 2, 3, 4]
#Notes
#Single-digit numbers should be ordered the same regardless of direction.
#Numbers in the list should be kept the same order.