#Factorial of a Positive Integer
#Write a function that takes a positive integer and return its factorial.
#The factorial of 0 is 1.
#The factorial of any positive integer Z is Z * (Z - 1) * (Z - 2) * . . . . . . * 1 (e.g. factorial of 3 is 3 * 2 * 1 = 6).
from Edabit.Test import Test
import math
def factorial(n):
    return math.factorial(n)

Test.assert_equals(factorial(4), 24)
Test.assert_equals(factorial(0), 1)
Test.assert_equals(factorial(9), 362880)
Test.assert_equals(factorial(1), 1)
Test.assert_equals(factorial(2), 2)
