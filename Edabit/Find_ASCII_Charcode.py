#Find ASCII Charcode of Inverse Case Character
#Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.
#Notes
#The argument will always be a single character.
#Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.
def counterpartCharCode(char):
    if char.isupper():
        t=char.lower()
        return ord(t)
    else:
        c=char.upper()
        return ord(c)
#Given that:
  #- "A" char code is: 65
  #- "a" char code is: 97
print(counterpartCharCode("A") )
#➞ 97
print(counterpartCharCode("a") )
#➞ 65
