#Remove Repeated Letters
#Create a function which replaces all repeated letters in a word with single letters.
import itertools
def remove_repeats(string):
    r=[]
    for i in string:
        if r[-1]!=i:
            r.append(i)
    return ''.join(r)

print(remove_repeats("aaabbbccc") )
#➞ "abc"

print(remove_repeats("bookkeeper"))
#➞ "bokeper"

print(remove_repeats("nananana") )
#➞ "nananana"
