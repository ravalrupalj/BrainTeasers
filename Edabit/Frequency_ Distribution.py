#Create a function that returns the frequency distribution of a list. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.


def get_frequencies(lst):
    dict = {}
    for i in lst:
        if dict.get(i):
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
#OR
#from collections import*
#return counter(lst)

print(get_frequencies(["A", "B", "A", "A", "A"]))
# { "A" : 4, "B" : 1 }
print(get_frequencies([1, 2, 3, 3, 2]))
# { 1: 1, 2: 2, 3: 2 }
print(get_frequencies([True, False, True, False, False]))
# { True: 2, False: 3 }
print(get_frequencies([]))
# {}
