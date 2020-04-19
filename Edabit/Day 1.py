#Fraction Greater Than One

#Given a fraction as a string, return whether or not it is greater than 1 when evaluated.
#greater_than_one("1/2") ➞ False
#greater_than_one("7/4") ➞ True
#greater_than_one("10/10") ➞ False

#Fractions must be strictly greater than 1 (see example #3).

from fractions import Fraction

def greater_than_one(frac):
    return eval(frac)>1
    #or
    #return float(sum(Fraction(s) for s in frac.split()))


print(greater_than_one("1/2"))
print(greater_than_one("7/4"))