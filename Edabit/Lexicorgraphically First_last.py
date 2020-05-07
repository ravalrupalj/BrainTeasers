#Lexicographically First and Last
#Write a function that returns the lexicographically first and lexicographically last rearrangements of a string. Output the results in the following manner:
#first_and_last(string) ➞ [first, last]
#Lexicographically first: the permutation of the string that would appear first in the English dictionary (if the word existed).
#Lexicographically last: the permutation of the string that would appear last in the English dictionary (if the word existed).
def first_and_last(s):
    t=sorted(s)
    e=''.join(t)
    r=e[::-1]
    p=e,r
    return list(p)


print(first_and_last("marmite"))
#➞ ["aeimmrt", "trmmiea"]
print(first_and_last("bench"))
#➞ ["bcehn", "nhecb"]
print(first_and_last("scoop"))
#➞ ["coops", "spooc"]
