#Which Number Is Not like the Others?
#Create a function that takes a list of numbers and return the number that's unique.
#Notes
#est cases will always have exactly one unique number while all others are the same.
import numpy
def unique(lst):
    for i in lst:
        if lst.count(i)==1:
            return i

print(unique([3, 3, 3, 7, 3, 3]))
#➞ 7
print(unique([0, 0, 0.77, 0, 0]))
#➞ 0.77
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))
#➞ 0
