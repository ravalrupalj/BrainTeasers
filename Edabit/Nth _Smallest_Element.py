#Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).
#Notes
#n will always be >= 1.
#Each number in the array will be distinct (there will be a clear ordering).
#Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest element, return None.
def nth_smallest(lst, n):
    t=sorted(lst)
    if len(t)>=n:
        return t[n-1]
    else:
        return None
print(nth_smallest([1, 3, 5, 7], 1))
#➞ 1
print(nth_smallest([1, 3, 5, 7], 3))
#➞ 5
print(nth_smallest([1, 3, 5, 7], 5))
#➞ None
print(nth_smallest([7, 3, 5, 1], 2))
#➞ 3
