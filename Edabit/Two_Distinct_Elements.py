#Two Distinct Elements
#In each input list, every number repeats at least once, except for two.
#Write a function that returns the two unique numbers.
#Keep the same ordering in the output.
def returnUnique(list):
    l=[]
    for i in list:
        if list.count(i)==1:
            l.append(i)
    return l

print(returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) )
#➞ [9, 7]
print(returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) )
#➞ [2, 1]
print(returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) )
#➞ [5, 6]

