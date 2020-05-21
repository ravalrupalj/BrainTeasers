#Box Completely Filled?
#Create a function that checks if the box is completely filled with the asterisk symbol *.
#Boxes of size n <= 2 are considered automatically filled (see example #4).
def completely_filled(lst):
    for i in lst:
        if ' ' in i:
            return False
    return True
print(completely_filled(["#####", "#***#","#***#", "#***#", "#####"]))
#➞ True
print(completely_filled([ "#####", "#* *#","#***#","#***#", "#####"]))
#➞ False
print(completely_filled(["###", "#*#","###"]))
#➞ True
print(completely_filled(["##","##"]))
#➞ True
#Notes
#Boxes of size n <= 2 are considered automatically filled (see example #4).