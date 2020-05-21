#Stupid Addition
#Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.
#Notes
#If the two parameters are different data types, return None.
#All parameters will either be strings or integers.
def stupid_addition(a,b):
    if type(a)!=type(b):
        return None
    else:
        if type(a)==int:
            return str(a)+str(b)
        else:
            return int(a)+int(b)


print(stupid_addition(1, 2) )
#➞ "12"

print(stupid_addition("1", "2"))
#➞ 3

print(stupid_addition("1", 2) )
#➞ None
