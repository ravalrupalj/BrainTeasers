#The Fibonacci Number
#Create a function that, given a number, returns the corresponding Fibonacci number.

#Examples
def fibonacci(num):
    l=[1,1]
    for i in l:
        t=l[-1]+l[-2]
        l.append(t)
        if len(l)==num+1:
            return l[-1]

print(fibonacci(3) )
#➞ 3
print(fibonacci(7) )
#➞ 21
print(fibonacci(12))
#➞ 233
#Notes
#The first number in the sequence starts at 1 (not 0).

