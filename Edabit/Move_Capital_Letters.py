#Move Capital Letters to the Front
#Create a function that moves all capital letters to the front of a word.
# #Keep the original relative order of the upper and lower case letters the same.
def cap_to_front(s):
    l=[]
    r=[]
    for i in s:
        if i.isupper():
            l.append(i)
    t=''.join(l)
    for i in s:
        if i.islower():
            r.append(i)
    c=''.join(r)
    return t+c
print(cap_to_front("hApPy"))
#➞ "APhpy"
print(cap_to_front("moveMENT"))
#➞ "MENTmove"
print(cap_to_front("shOrtCAKE"))
#➞ "OCAKEshrt"
