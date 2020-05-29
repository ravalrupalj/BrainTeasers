#Sum of Decimals
#Captain Obvious is asked to implement a simple function that given two decimal numbers A and B returns their sum.
#"Easy one!" he thinks, but soon he discovers that his function fails over the fifty percent of given test cases! He suspects the test cases are wrong, but his calculator is saying they're correct! What's happening?
#Can you help Captain Obvious to debug his function and solve the exercise?
#Given numbers can be either integer or float with 1 up to 6 decimals.
#Don't round results!
#Bonus: Can you resolve it using a simple math expression instead of a built-in method?
import decimal
def float_sum(a,b):

    t=decimal.Decimal(str(a)) + decimal.Decimal(str(b))
    string=decimal.Decimal(t).normalize()
    return float(string)

print(float_sum(0.3, 0.7) )
#➞ 1

print(float_sum(0.35, 0.75))
#➞ 1.1

print(float_sum(1.234, 5.6789))
#➞ 6.9129
