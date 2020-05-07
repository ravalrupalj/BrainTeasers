#Is the String in Order?
#Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
#You don't have to handle empty strings.
def is_in_order(txt):
    t=''.join(sorted(txt))
    return t==txt
print(is_in_order("abc"))
#➞ True
print(is_in_order("edabit"))
#➞ False
print(is_in_order("123"))
#➞ True
print(is_in_order("xyzz"))
#➞ True
