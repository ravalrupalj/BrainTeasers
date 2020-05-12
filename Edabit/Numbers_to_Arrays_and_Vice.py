#Numbers to Arrays and Vice Versa
#Write two functions:
#to_list(), which converts a number to a list of its digits.
#to_number(), which converts a list of digits back to its number.
#All test cases will be weakly positive numbers: >= 0
def to_list(num):
    l=[]
    for i in str(num):
        l.append(int(i))
    return l

def to_number(lst):
    s=''
    for i in lst:
        s=s+str(i)
    return int(s)
print(to_list(235) )
#➞ [2, 3, 5]
print(to_list(0) )
#➞ [0]
print(to_number([2, 3, 5]) )
#➞ 235
print(to_number([0]))
#➞ 0
