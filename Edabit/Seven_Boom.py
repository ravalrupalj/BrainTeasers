#Seven Boom!
#Create a function that takes a list of numbers and return "Boom!" if the number 7 appears in the list. Otherwise, return "there is no 7 in the list".

def seven_boom(lst):
    string=''
    for i in lst:
        string=string+str(i)
    if '7' in string:
        return 'Boom!'
    else:
        return 'there is no 7 in the list'
print(seven_boom([1, 2, 3, 4, 5, 6, 7]))
#➞ "Boom!"

print(seven_boom([8, 6, 33, 100]))
#➞ "there is no 7 in the list"

print(seven_boom([2, 55, 60, 97, 86]))
#➞ "Boom!"
