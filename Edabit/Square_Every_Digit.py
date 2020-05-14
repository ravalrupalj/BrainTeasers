#Square Every Digit
#Create a function that squares every digit of a number.
#The function receives an integer and must return an integer.
def square_digits(n):
    a=str(n)
    s=[]
    for i in a:
        s.append(int(i)**2)
    r=''
    for i in s:
        r=r+str(i)
    return int(r)




print(square_digits(9119) )
#➞ 811181

print(square_digits(2483) )
#➞ 416649

print(square_digits(3212) )
#➞ 9414

