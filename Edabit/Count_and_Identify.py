#Count and Identify Data Types
#Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
#List order is:
#[int, str, bool, list, tuple, dictionary]
def count_datatypes(*args):
    d={'int':0,'str':0,'bool':0,'list':0,'tuple':0,'dictionary':0}
    for i in args:
        if isinstance(i,bool):
            d['bool']=d['bool']+1
        elif isinstance(i,int):
            d['int']=d['int']+1
        elif isinstance(i,str):
            d['str']=d['str']+1
        elif isinstance(i,list):
            d['list']=d['list']+1
        elif isinstance(i,tuple):
            d['tuple']=d['tuple']+1
        elif isinstance(i,dict):
            d['dictionary']=d['dictionary']+1
    return list(d.values())
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