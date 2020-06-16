#Combinations
#Create a function that takes a variable number of groups of items, and returns the number of ways the items can be arranged, with one item from each group. Order does not matter.
def combinations(*items):
    l=[]
    for t in items:
        l.append(str(t))
    multi = 1
    for i in l:
        if i=='0':
            continue
        multi = multi * int(i)
    return multi
print(combinations(6, 7, 0))
#42
print(combinations(2, 3, 4, 5, 6, 7, 8, 9, 10))
#3628800
print(combinations(2, 3) )
#➞ 6

print(combinations(3, 7, 4) )
#➞ 84

print(combinations(2, 3, 4, 5))
#➞ 120


