#Find the Fulcrum
#A fulcrum of a list is an integer such that all elements to the left of it and all elements to the right of it sum to the same value. Write a function that finds the fulcrum of a list.
def find_fulcrum(lst):
    for i in range(1,len(lst)-1):
        l_count=sum(lst[0:i])
        r_count=sum(lst[i+1:len(lst)])
        if l_count==r_count:
            return lst[i]

    return -1
print(find_fulcrum([3, 1, 5, 2, 4, 6, -1]))
#➞ 2
#// Since [3, 1, 5] and [4, 6, -1] both sum to 9
print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
#➞ 4
print(find_fulcrum([9, 1, 9]))
#➞ 1
print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))
#➞ 0
print(find_fulcrum([8, 8, 8, 8]))
#➞ -1
#Notes
#If the fulcrum does not exist, return -1 (see example #4).
#Exclude the leftmost and rightmost elements when computing the fulcrum (it doesn't make sense to sum zero values).
#If a list has multiple fulcrums, return the one that occurs first.