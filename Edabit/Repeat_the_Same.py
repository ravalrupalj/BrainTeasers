#Repeat the Same Item Multiple Times
#Create a function that takes two arguments (item, times). The first argument (item) is the item that needs repeating while the second argument (times) is the number of times the item is to be repeated. Return the result in a list.
#item can be either a string or a number.
#times will always be a number.
def repeat(item,times):
    l=[]
    for i in range(0,times):
        l.append(item)
    return l

print(repeat("edabit", 3) )
#➞ ["edabit", "edabit", "edabit"]

print(repeat(13, 5) )
#➞ [13, 13, 13, 13, 13]

print(repeat("7", 2) )
#➞ ["7", "7"]

print(repeat(0, 0) )
#➞ []

