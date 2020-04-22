#Palindrome?
#A palindrome is a word that is identical forward and backwards.
#Given a word, create a function that checks whether it is a palindrome.
#mom
#racecar
#kayak
#All test input is lower cased.
#is_palindrome("mom") ➞ True
#is_palindrome("scary") ➞ False
#is_palindrome("reviver") ➞ True
#is_palindrome("stressed") ➞ False
def is_palindrome(txt):
    return txt==txt[::-1]

print(is_palindrome("mom"))
print(is_palindrome("scary") )
print(is_palindrome("reviver"))
print(is_palindrome("stressed"))