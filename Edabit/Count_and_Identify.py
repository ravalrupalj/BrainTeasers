#Count and Identify Data Types
#Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
#List order is:
#[int, str, bool, list, tuple, dictionary]
def count_datatypes(*args):
    lst=[type(i) for i in args]
    return  [lst.count(i) for i in (int, str, bool, list, tuple, dict)]
print(count_datatypes(1, 45, "Hi", False) )
#➞ [2, 1, 1, 0, 0, 0]

print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) )
#➞ [3, 0, 0, 1, 1, 0]

print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) )
#➞ [2, 2, 3, 1, 0, 2]

print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) )
#➞ [2, 0, 1, 2, 2, 0]
#Notes
#If no arguments are given, return [0, 0, 0, 0, 0, 0]