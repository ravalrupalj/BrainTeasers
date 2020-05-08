#Amplify the Multiples of Four
#Create a function that takes an integer and returns a list from 1 to the given number, where:
#If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
#If the number cannot be divided evenly by 4, simply return the number.
#The given integer will always be equal to or greater than 1.
#Include the number (see example above).
#To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult, just solve the challenge any way you can.
def amplify(num):
    l=[]
    for i in range(1,num+1):
        if i%4==0:
            l.append(i*10)
        else:
            l.append(i)
    return l
print(amplify(4))
#➞ [1, 2, 3, 40]

print(amplify(3) )
#➞ [1, 2, 3]

print(amplify(25) )
#➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]

