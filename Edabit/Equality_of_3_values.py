#Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
#Your function must return 0, 2 or 3.
from Edabit.Test import Test

def equal(a, b, c):
    if a==b and b==c and c==a:
        return 3
    elif a!=b and b!=c and c!=a:
        return 0
    elif a==b and b!=c:
        return 2
    elif b==c and a!=b:
        return 2
    elif a==c and b!=c:
        return 2
Test.assert_equals(equal(2,3,4), 0, "All values are differents")
Test.assert_equals(equal(7,3,7), 2, "Two values are equal")
Test.assert_equals(equal(4,4,4), 3, "All 3 values are equal")
Test.assert_equals(equal(7,3,4), 0, "All values are differents")
Test.assert_equals(equal(3,3,6), 2, "Two values are equal")
Test.assert_equals(equal(1,1,1), 3, "All 3 values are equal")
Test.assert_equals(equal(1,7,6), 0, "All values are differents")
Test.assert_equals(equal(7, 7, 7), 3, "All 3 values are equal")
Test.assert_equals(equal(6, 3, 3), 2, "Two values are equal")