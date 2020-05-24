#Concatenate Variable Number of Input Lists
#Create a function that concatenates n input lists, where n is variable.
#Notes
#Lists should be concatenated in order of the arguments.
def concat(*args):
    l=[]
    for i in args:
        for t in i:
            l.append(t)
    return l


print(concat([1, 2, 3], [4, 5], [6, 7]))
#➞ [1, 2, 3, 4, 5, 6, 7]

print(concat([1], [2], [3], [4], [5], [6], [7]) )
#➞ [1, 2, 3, 4, 5, 6, 7]

print(concat([1, 2], [3, 4]) )
#➞ [1, 2, 3, 4]

print(concat([4, 4, 4, 4, 4]) )
#➞ [4, 4, 4, 4, 4]
