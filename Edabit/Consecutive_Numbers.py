#Consecutive Numbers
#Create a function that determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once.
def cons(lst):
    minimum=min(lst)
    maximum=max(lst)
    new_lst=sorted(lst)
    l=[]
    for i in lst:
        if lst.count(i)>1:
            return False
    for i in range(minimum,maximum+1):
        l.append(i)
    if l==new_lst:
        return True
    else:
        return False

print(cons([5, 1, 4, 3, 2]))
#➞ True
#// Can be re-arranged to form [1, 2, 3, 4, 5]

print(cons([5, 1, 4, 3, 2, 8]))
#➞ False

print(cons([5, 6, 7, 8, 9, 9]))
#➞ False
#// 9 appears twice
