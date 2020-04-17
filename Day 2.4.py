#Reverse and Capitalize
#Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.
#reverse_capitalize("abc") ➞ "CBA"
#reverse_capitalize("hellothere") ➞ "EREHTOLLEH"
#reverse_capitalize("input") ➞ "TUPNI"
def reverse_capitalize(txt):
    t=txt.upper()
    return t[::-1]

print(reverse_capitalize("abc") )
print(reverse_capitalize("hellothere"))
print(reverse_capitalize("input"))