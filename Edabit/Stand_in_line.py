#Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.
#For an empty list input, return: "No list has been selected"
def next_in_line(lst, num):
    if len(lst)>0:
        t=lst.pop(0)
        r=lst.append(num)
        return lst
    else:
        return 'No list has been selected'
print(next_in_line([5, 6, 7, 8, 9], 1))
#➞ [6, 7, 8, 9, 1]
print(next_in_line([7, 6, 3, 23, 17], 10))
#➞ [6, 3, 23, 17, 10]
print(next_in_line([1, 10, 20, 42 ], 6))
#➞ [10, 20, 42, 6]
print(next_in_line([], 6))
#➞ "No list has been selected"

