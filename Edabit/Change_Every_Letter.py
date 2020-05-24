#Change Every Letter to the Next Letter
#Write a function that changes every letter to the next letter:
#"a" becomes "b"
#"b" becomes "c"
#"d" becomes "e"
#and so on ...
#Notes
#There will be no z's in the tests.
import string
def move(word):
    newword=''
    for i in word:
        newword=newword+chr(ord(i)+1)
    return newword

print(move("hello") )
#➞ "ifmmp"
print(move("bye") )
#➞ "czf"
print(move("welcome") )
#➞ "xfmdpnf"
