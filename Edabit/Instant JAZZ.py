def jazzify(lst):
    l=[]
    for i in lst:
        if i[-1] not in '7':
            l.append(i+'7')
        else:
            l.append(i)
    return l

print(jazzify(["G", "F", "C"]) )
#➞ ["G7", "F7", "C7"]

print(jazzify(["Dm", "G", "E", "A"]))
#➞ ["Dm7", "G7", "E7", "A7"]

print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
#➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

print(jazzify([]) )
#➞ []