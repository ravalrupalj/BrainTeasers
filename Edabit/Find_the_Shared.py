#Find the Shared Letters between Two Strings
#Given two strings, return a string containing only the letters shared between the two.
#Notes
#If none of the letters are shared, return an empty string.
#The function should be case insensitive (e.g. comparing A and a should return a).
#Sort the resulting string alphabetically before returning it.
def shared_letters(a, b):
    s=''
    t=set(a.lower())
    for i in t:
        if i in b.lower():
            s=s+i

    return ''.join(sorted(s))
print(shared_letters('Aa', 'aA'))
 #'a'
print(shared_letters("house", "home"))
#➞ "eho"
print(shared_letters("Micky", "mouse"))
#➞ "m"
print(shared_letters("house", "villa"))
#➞ ""
