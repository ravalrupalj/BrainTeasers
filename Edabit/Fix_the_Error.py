#Remove all vowels
def remove_vowels(st):
    l=['a','e','i','o','u']
    ls=[]
    for i in st:
        if i not in l:
            ls.append(i)
    return ''.join(ls)

def remove_vowels(string):
    vowels = "aeiou"
    for vowel in vowels:
        string=string.replace(vowel, "", )
    return string

print(remove_vowels("ben") )
#➞ "bn"

print(remove_vowels("hello") )
#➞ "hllo"
# The "e" is removed, but the "o" is still there!

print(remove_vowels("apple") )
#➞ "appl"
# The "e" is removed, but the "a" is still there!