#Both Zero, Negative or Positive
#Write a function that checks if two numbers are:
#Smaller than 0
#Greater than 0
#Exactly 0
#Examples
#both(6, 2) ➞ True
#both(0, 0) ➞ True
#both(-1, 2) ➞ False
#both(0, 2) ➞ False
def both(n1, n2):
    if n1<0 and n2<0:
        return True
    elif n1==0 and n2==0:
        return True
    elif n1>0 and n2>0:
        return True
    else:
        return False

print(both(6, 2))
print(both(0, 0))
print(both(-1, 2))
print(both(0, 2))