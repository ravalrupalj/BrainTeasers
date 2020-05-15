#Return the Highest and Lowest Numbers
#Create a function that accepts a string of space separated integers and returns the highest and lowest integers (as a string).

#All integers are valid, no need to validate them.
#There will always be at least one integer in the input string.
#Output string must be two integers separated by a single space, and highest number is first.
def high_low(string):
    l=[]
    for i in string.split( ):
        l.append(int(i))
    new= sorted(l)
    new_max=str(new[-1])
    new_min=str(new[0])
    new_string=new_max+' '+new_min
    return new_string


print(high_low("1 2 3 4 5") )
#➞ "5 1"
print(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
#"542 -214"
print(high_low("1 2 -3 4 5") )
#➞ "5 -3"
print(high_low("1 9 3 4 -5"))
#➞ "9 -5"
print(high_low("13") )
#➞ "13 13"
