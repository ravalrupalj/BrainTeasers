#Number of Lists in a List
#Return the total number of lists inside a given list.
def num_of_sublists(lst):
    count=0
    for i in lst:
        if type(i)==list:
            count=count+1
    return count
print(num_of_sublists([[1, 2, 3]]))
#➞ 1

print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
#➞ 3

print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
#➞ 4

print(num_of_sublists([1, 2, 3]))
#➞ 0
