#Recursion: Length of a String
#Write a function that returns the length of a string. Make your function recursive.
#Check the Resources tab for info on recursion.
def length(txt):
    if len(txt)==0:
        return 0
    first_len=len(txt[0])
    return first_len+length(txt[1:])
print(length("apple") )
#➞ 5
print(length("make") )
#➞ 4
print(length("a") )
#➞ 1
print(length("") )
#➞ 0

