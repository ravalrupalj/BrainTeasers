#Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
from Edabit.Test import Test
def filter_list(l):
    return [i for i in l if not isinstance(i,str)]


Test.assert_equals(filter_list([1, 2, 3, "a", "b", 4]), [1, 2, 3, 4])
Test.assert_equals(filter_list(["A", 1, '&amp', 0, -9, 'Edabit']), [1, 0, -9])