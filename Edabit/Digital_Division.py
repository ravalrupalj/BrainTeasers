#Digital Division
#In this challenge, you have to verify if a number is exactly divisible by a combination of its digits. There are three possible conditions to test:

#The given number is exactly divisible by each of its digits excluding the zeros.
#The given number is exactly divisible by the sum of its digits.
#The given number is exactly divisible by the product of its digits.
#Given an integer n, implement a function that returns:

#If every test is true, a string "Perfect".
#If some test is true, the number of true tests (1 or 2).
#If every test is false, a string "Indivisible".
def digital_division(num):
    l=[]
    count=0
    prod=1
    string_num=str(num)
    for i in string_num:
        if int(i)==0:
            pass
        elif not num%int(i)==0:
            l.append("No")
            break
    if "No" not in l:
        l.append("Yes")
    for j in string_num:
        count=count+int(j)
    if num%count==0:
        l.append("Yes")
    else:
        l.append("No")
    for e in string_num:
        prod=prod*int(e)

    if prod==0:
        l.append("No")
    elif num%prod==0:
        l.append("Yes")
    else:
        l.append("No")

    if  len(set(l))==1 and "Yes" in l:
        return "Perfect"
    elif len(set(l))==1 and "No" in l:
        return "Indivisible"
    elif l.count("Yes") == 2 and l.count("No")==1:
        return 2
    else:
        return 1




print(digital_division(21) )
#➞ 1
# Exactly divisible only by the sum of its digits (2 + 1 = 3).

print(digital_division(128))
#➞ 2
# Exactly divisible by each of its digits.
# Exactly divisible by the product of its digits (1 * 2 * 8 = 16).

print(digital_division(100) )
#➞ 2
# Exactly divisible by each of its digits (excluding zeros).
# Exactly divisible by the sum of its digits (1 + 0 + 0 = 1).

print(digital_division(12))
#➞ "Perfect"
# Exactly divisible by each of its digits.
# Exactly divisible by 3 (sum of digits = 1 + 2).
# Exactly divisible by 2 (product of digits = 1 * 2).

print(digital_division(31) )
#➞ "Indivisible"
# Every testing condition is false.
#Notes
#Remember to exclude any 0-digit when testing if the given n is divisible by each of its digits (see example #3).
#A number containing at least a 0-digit can't be exactly divided by the product of its digits (division by 0).
#Trivially, every single-digit positive number greater than 0 is Perfect
#Any given number will be a positive integer greater than 0.