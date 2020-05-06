#Say Hello to Guests
#In this exercise you will have to:
#Take a list of names.
#Add "Hello" to every name.
#Make one big string with all greetings.
#The solution should be one string with a comma in between every "Hello (Name)".
#Each greeting has to be separated with a comma and a space.
#If you're given an empty list [], return an empty string "".
def greet_people(names):
    r=[]
    for i in names:
        t=('Hello '+i)
        r.append(t)
    return ', '.join(r)
print(greet_people(["Joe"]))
#➞ "Hello Joe"
print(greet_people(["Angela", "Joe"]) )
#➞ "Hello Angela, Hello Joe"
print(greet_people(["Frank", "Angela", "Joe"]) )
#➞ "Hello Frank, Hello Angela, Hello Joe"
