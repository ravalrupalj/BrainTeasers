#Evaluating Factorials
#Create a function that takes a list of factorial expressions and returns the sum.
#Notes
#0! and 1! both equal 1.
def eval_factorial(lst):
    import math
    sum = 0
    for i in lst:
        t=i[:-1]
        sum += math.factorial(int(t))
    return sum



print(eval_factorial(["2!", "3!"]) )
#➞ 8

print(eval_factorial(["5!", "4!", "2!"]) )
#➞ 146

print(eval_factorial(["0!", "1!"]) )
#➞ 2
