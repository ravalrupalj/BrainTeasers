#Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.
#Return a boolean value (True or False).
#The string can contain any character.
#When no x and no o are in the string, return True.
#Notes
#Remember to return True if there aren't any x's or o's.
#Must be case insensitive.
from Edabit.Test import Test


def XO(str):
    t=str.lower()
    return t.count('o')==t.count('x')


Test.assert_equals(XO("ooxx"), True)
Test.assert_equals(XO("xooxx"), False)
Test.assert_equals(XO("ooxXm"), True)
Test.assert_equals(XO("zpzpzpp"), True)
Test.assert_equals(XO("zzoo"), False)
Test.assert_equals(XO("Xo"), True)
Test.assert_equals(XO("o"), False)
Test.assert_equals(XO("xxxoo"), False)
Test.assert_equals(XO(""), True)