#Characters and ASCII Code Dictionary
#Write a function that transforms a list of characters into a list of dictionaries, where:

#The keys are the characters themselves.
#The values are the ASCII codes of those characters.
def to_dict(lst):
    l=[]
    for i in lst:
        di={}
        di[i]=ord(i)
        l.append(di)
    return l

print(to_dict(["a", "b", "c"]) )
#➞ [{"a": 97}, {"b": 98}, {"c": 99}]

print(to_dict(["^"]) )
#➞ [{"^": 94}]

print(to_dict([]) )
#➞ []
