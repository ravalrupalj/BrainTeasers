#Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
import operator
def reverse(name):
    if isinstance(name,bool):
        if name==True:
            return False
        elif name==False:
            return True
    else:
        return 'boolean expected'

print(reverse(True))
#➞ False
print(reverse(False))
#➞ True
print(reverse(0))
#➞ "boolean expected"
print(reverse(None) )
#➞ "boolean expected"
