#Correct Inequality Signs
#Create a function that returns true if a given inequality expression is correct and false otherwise.
def correct_signs(string):
    return eval(string)

print(correct_signs("3 < 7 < 11"))
#➞ True

print(correct_signs("13 > 44 > 33 > 1"))
#➞ False

print(correct_signs("1 < 2 < 6 < 9 > 3"))
#➞ True
