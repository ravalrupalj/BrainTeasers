def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)


print(factorial(5) )
#➞ 120

print(factorial(3) )
#➞ 6

print(factorial(2))
#➞ 2