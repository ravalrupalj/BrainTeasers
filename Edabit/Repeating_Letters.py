#Create a function that takes a string and returns a string in which each character is repeated once.
#All test cases contain valid strings. Don't worry about spaces, special characters or numbers. They're all considered valid characters.
def double_char(txt):
    l=[]
    for i in txt:
        l.append(i*2)
    return ''.join(l)

print(double_char("String") )
#➞ "SSttrriinngg"
print(double_char("Hello World!") )
#➞ "HHeelllloo  WWoorrlldd!!"
print(double_char("1234!_ ") )
#➞ "11223344!!__  "
