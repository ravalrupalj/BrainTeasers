#The Fibonacci Number
#Create a function that, given a number, returns the corresponding Fibonacci number.
#The first number in the sequence starts at 1 (not 0).
def fibonacci(num):
    a=0
    b=1
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c

    return c


print(fibonacci(3) )
#➞ 3
print(fibonacci(7))
#➞ 21
print(fibonacci(12))
#➞ 233

