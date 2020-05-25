#Order by Length First
#Graded lexicographic order (grlex order for short) is a way of ordering words that:

#First orders words by length.
#Then orders words of the same size by their dictionary order.
#For example, in grlex order:

#"tray" < "trapped" since "tray" has lenght 4 while "trapped" has lenght 7.
#"trap" < "tray" since both have lenght 4, but "trap" comes before "tray" in the dictionary.
#Given a list of words, return that list in grlex order.
from itertools import permutations
def make_grlex(lst):
    a=sorted(lst)
    b=sorted(a,key=len)
    return b
print(make_grlex(["small", "big"]))
#➞ ["big", "small"]

print(make_grlex(["cat", "ran", "for", "the", "rat"]))
#➞ ["cat", "for", "ran", "rat", "the"]

print(make_grlex(["this", "is", "a", "small", "test"]))
#➞ ["a", "is", "test", "this", "small"]
