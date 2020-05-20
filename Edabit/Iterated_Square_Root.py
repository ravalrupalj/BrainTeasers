#Iterated Square Root
#The iterated square root of a number is the number of times the square root function must be applied to bring the number strictly under 2.
#Given an integer, return its iterated square root. Return "invalid" if it is negative.
#Idea for iterated square root by Richard Spence.
import math
def i_sqrt(n):
    if n < 0: return 'invalid'
    count = 0
    while n >= 2:
        n **= 0.5
        count += 1
    return count



print(i_sqrt(1))
#➞ 0
print(i_sqrt(2))
#➞ 1
print(i_sqrt(7))
#➞ 2
print(i_sqrt(27))
#➞ 3
print(i_sqrt(256))
#➞ 4
print(i_sqrt(-1) )
#➞ "invalid"

