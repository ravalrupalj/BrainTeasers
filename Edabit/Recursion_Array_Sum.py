#Recursion: Array Sum
#Write a function that finds the sum of a list. Make your function recursive.
#Return 0 for an empty list.
#Check the Resources tab for info on recursion.
def sum_recursively(lst):
    if len(lst)==0:
        return 0
    return lst[0]+sum_recursively(lst[1:])


print(sum_recursively([1, 2, 3, 4]))
#➞ 10
print(sum_recursively([1, 2]) )
#➞ 3
print(sum_recursively([1]) )
#➞ 1
print(sum_recursively([]) )
#➞ 0
