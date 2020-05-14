#Is Sam with Frodo?
#Sam and Frodo need to be close. If they are side by side in the list, your function should return True. If there is a name between them, return False.
#No matter who comes first, the result must be True if Frodo and Sam are side by side.
#There is only one Sam and one Frodo in the list.
def middle_earth(lst):
    a=lst.index('Frodo')
    b=lst.index('Sam')
    return a-b==-1 or a-b==1
print(middle_earth(["Frodo", "Sam", "Gandalf"]) )
#➞ True
print(middle_earth(["Frodo", "Saruman", "Sam"]))
#➞ False
print(middle_earth(["Orc", "Sam", "Frodo", "Legolas"]) )
#➞ True

