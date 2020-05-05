#Map the Letters in a String
#Given a word, create a dictionary that stores the indexes of each letter in a list.
#Make sure the letters are the keys.
#Make sure the letters are symbols.
#Make sure the indexes are stored in a list and those lists are values.
#Notes
#All strings given will be lowercase.
from collections import defaultdict
def map_letters(word):
    d = {}
    for char in word:
        ind = [i for i, a in enumerate(word) if a==char]
        if char not in d:
           d[char] = ind
    return d
    #return {i:[word.index(i)] for i in word}



    #return {v:index for index,v in enumerate(word)}# if
print(map_letters("dodo") )
#➞ { "d": [0, 2], "o": [1, 3] }

print(map_letters("froggy"))
#➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

print(map_letters("grapes"))
#➞ { "g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5] }
