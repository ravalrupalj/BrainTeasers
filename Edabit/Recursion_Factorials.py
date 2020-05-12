#Recursion: Factorials
#Write a function that calculates the factorial of a number recursively.
def factorial(n):
    count=1
    for i in range(1,n+1):
        count=count*i
    return count

print(factorial(5) )
#➞ 120

print(factorial(3) )
#➞ 6

print(factorial(1))
#➞ 1

print(factorial(0))
#➞ 1



