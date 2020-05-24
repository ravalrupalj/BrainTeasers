#Emptying the Values
#Given a list of values, return a list with each value replaced with the empty value of the same type.

#More explicitly:

#Replace integers (e.g. 1, 3), whose type is int, with 0
#Replace floats (e.g. 3.14, 2.17), whose type is float, with 0.0
#Replace strings (e.g. "abcde", "x"), whose type is str, with ""
#Replace booleans (True, False), whose type is bool, with False
#Replace lists (e.g. [1, "a", 5], [[4]]), whose type is list, with []
#Replace tuples (e.g. (1,9,0), (2,)), whose type is tuple, with ()
#Replace sets (e.g. {0,"a"}, {"b"}), whose type is set, with set()
#Caution: Python interprets {} as the empty dictionary, not the empty set.
#None, whose type is NoneType, is preserved as None
#Notes
#None has the special NoneType all for itself.
def empty_values(lst):
    l=[]
    for i in lst:
        if type(i)==int:
            l.append(0)
        elif type(i)==float:
            l.append(0.0)
        elif type(i)==str:
            l.append('')
        elif type(i)==bool:
            l.append(False)
        elif type(i)==list:
            l.append([])
        elif type(i)==tuple:
            l.append(())
        elif type(i)==set:
            l.append(set())
        else:
            l.append(None)
    return l


print(empty_values([1, 2, 3]) )
#➞ [0, 0, 0]

print(empty_values([7, 3.14, "cat"]) )
#➞ [0, 0.0, ""]

print(empty_values([[1, 2, 3], (1,2,3), {1,2,3}]) )
#➞ [[], (), set()]

print(empty_values([[7, 3.14, "cat"]]))
#➞ [[]]

print(empty_values([None]) )
#➞ [None]
