#Automorphic Numbers
#A number n is automorphic if n^2 ends in n.
#For example: n=5, n^2=25
#Create a function that takes a number and returns True if the number is automorphic, False if it isn't.
def is_automorphic(num):
    t=str(num**2)
    st=str(num)
    l=len(st)
    a=int('-'+str(l))
    if st==t[a:]:
        return True
    else:
        return False
print(is_automorphic(100))
#➞ False
print(is_automorphic(25) )
#➞ True
print(is_automorphic(36))
#➞ False
