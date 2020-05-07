#Create a function that takes a string and returns a string with its letters in alphabetical order.
#You can assume numbers and punctuation symbols won't be included in test cases. You'll only have to deal with single word, alphabetic characters.
def alphabet_soup(txt):
    t=sorted(txt)
    return ''.join(t)

print(alphabet_soup("hello") )
#➞ "ehllo"

print(alphabet_soup("edabit") )
#➞ "abdeit"

print(alphabet_soup("hacker"))
#➞ "acehkr"

print(alphabet_soup("geek") )
#➞ "eegk"

print(alphabet_soup("javascript") )
#➞ "aacijprstv"
