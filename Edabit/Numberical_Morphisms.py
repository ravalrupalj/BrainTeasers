#Numerical Morphisms
#A number num, that elevated to the power of another number k "ends" with the same num, it's automorphic.

#5² = 25
# It's automorphic because "25" ends with "5"

#5³  = 125
# It's automorphic because "125" ends with "5"

#76⁴ = 33362176
# It's automorphic because "33362176" ends with "76"
#A number can have various powers that make it automorphic (i.e. look at number 5 in the above example). In this challenge, you have to verify if the given number is automorphic for each power from 2 up to 10.

#Given a non-negative integer num, implement a function that returns the string:

#"Polymorphic" if num is automorphic for every power from 2 up to 10.
#"Quadrimorphic" if num is automorphic for only four powers (any from 2 up to 10).
#"Dimorphic" if num is automorphic for only two powers (any from 2 up to 10).
#"Enamorphic" if num is automorphic for only one power (any from 2 up to 10).
#"Amorphic" if num is not automorphic for for any powers from 2 up to 10.
#Notes
#You can do a complete loop cycle to check if num is automorphic for each power, or you can try to spot the discriminants that permit you to shorten the logic of your code.
#Despite being inspired by the OEIS sequence A003226, the assertions of this challenge are to be considered properly valid only in the specific context.
#Examples
def power_morphic(n):
    l=[]
    count=0
    for i in range(2,11):
        t=n**i
        b=len(str(n))
        a=int(str(t)[-b:])
        if a==n:
            count=count+1

    if count==9:
        return 'Polymorphic'
    elif count==4:
        return 'Quadrimorphic'
    elif count==2:
        return 'Dimorphic'
    elif count==1:
        return 'Enamorphic'
    else:
        return 'Amorphic'


print(power_morphic(5) )
#➞ "Polymorphic"
# From 2 up to 10, every power of 5 ends with 5

print(power_morphic(21) )
#➞ "Enamorphic"
# 21⁶ = 85766121
print(power_morphic(7) )
#➞ "Dimorphic"
# 7⁵ = 716807
# 7⁹ = 40353607

print(power_morphic(4) )
#➞ "Quadrimorphic"
# 4³ = 64
# 4⁵ = 1024
# 4⁷ = 16384
# 4⁹ = 262144

print(power_morphic(10))
#➞ "Amorphic"
# There are no powers that make it automorphic
print(power_morphic(10) )
#Amorphic