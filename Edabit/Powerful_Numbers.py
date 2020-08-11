#Powerful Numbers
#Given a positive number x:

#p = (p1, p2, …)
# Set of *prime* factors of x
#If the square of every item in p is also a factor of x, then x is said to be a powerful number.
#Create a function that takes a number and returns True if it's powerful, False if it's not.
def is_powerful(num):
    return [d for d in num if isprime(d)]

print(is_powerful(36))
#➞ True
# p = (2, 3) (prime factors of 36)
# 2^2 = 4 (factor of 36)
# 3^2 = 9 (factor of 36)

print(is_powerful(27))
#➞ True

print(is_powerful(674))
#➞ False
#Notes
#N/A