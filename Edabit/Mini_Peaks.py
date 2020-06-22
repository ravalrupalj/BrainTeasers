#Mini Peaks
#Write a function that returns all the elements in an array that are strictly greater than their adjacent left and right neighbors.
def mini_peaks(lst):
    l=[]
    for i in range(1,len(lst)-1):
        if lst[i-1]<lst[i] and lst[i+1]<lst[i]:
            l.append(lst[i])
    return l
print(mini_peaks([4, 5, 2, 1, 4, 9, 7, 2]))
#➞ [5, 9]

print(mini_peaks([1, 2, 1, 1, 3, 2, 5, 4, 4]))
#➞ [2, 3, 5]

print(mini_peaks([1, 2, 3, 4, 5, 6]))
#➞ []
#Notes
#Do not count boundary numbers, since they only have one left/right neighbor.
#If no such numbers exist, return an empty array.