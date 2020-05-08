#A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.
#Create a function that takes in a list of names and returns the name of the secret society.
#The secret society's name should be entirely uppercased.
def society_name(lst):
    l=[]
    for i in lst:
        l.append(i[0])
    e=sorted(l)
    str=''.join(e)
    return str
print(society_name(["Adam", "Sarah", "Malcolm"]))
#➞ "AMS"

print(society_name(["Harry", "Newt", "Luna", "Cho"]))
#➞ "CHLN"

print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
#➞ "CJMPRR"
